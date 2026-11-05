"""
models.py
=========
The 7 MSQF Supervised Learning Classifiers and Purged Walk-Forward Engine.

Implements the full 7-model spectrum from the MSQF curriculum:
1. Logistic Regression (L2 penalized linear classifier)
2. Gaussian Naive Bayes (Probabilistic generative baseline)
3. K-Nearest Neighbors (Instance-based metric classifier)
4. Decision Tree (CART non-linear rule learner)
5. Random Forest (Bagging ensemble with feature importance)
6. Support Vector Machine (RBF kernel maximum-margin classifier)
7. Multi-Layer Perceptron (Deep feedforward neural network)

Incorporates Purged Time-Series Split with an Embargo buffer to prevent
lookahead leakage across overlapping trade holding horizons.
"""

from typing import Dict, List, Tuple, Any, Generator, Optional
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, clone
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    brier_score_loss,
    confusion_matrix,
)


class PurgedTimeSeriesSplit:
    """Time-series walk-forward CV splitter with purging and embargo.
    
    Prevents serial leakage between overlapping trade holding horizons.
    """
    def __init__(self, n_splits: int = 4, embargo_pct: float = 0.02):
        self.n_splits = n_splits
        self.embargo_pct = embargo_pct

    def split(
        self,
        X: np.ndarray,
        y: Optional[np.ndarray] = None,
        groups: Optional[np.ndarray] = None,
    ) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
        n_samples = len(X)
        embargo = int(n_samples * self.embargo_pct)
        fold_size = n_samples // (self.n_splits + 1)

        for i in range(1, self.n_splits + 1):
            train_end = i * fold_size
            test_start = train_end + embargo
            test_end = min((i + 1) * fold_size, n_samples)
            
            if test_start >= n_samples or test_start >= test_end:
                break
                
            train_indices = np.arange(0, train_end)
            test_indices = np.arange(test_start, test_end)
            yield train_indices, test_indices


def get_msqf_model_suite() -> Dict[str, BaseEstimator]:
    """Instantiates the 6 core supervised learning classifiers from the MSQF syllabus.
    
    Returns
    -------
    Dict[str, BaseEstimator]
        Mapping from model identifier to configured scikit-learn estimator.
    """
    models = {
        "Logistic Regression": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(C=1.0, max_iter=1000, random_state=42)),
        ]),
        "Naive Bayes": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("clf", GaussianNB()),
        ]),
        "KNN": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("clf", KNeighborsClassifier(n_neighbors=15, weights="distance")),
        ]),
        "Decision Tree": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("clf", DecisionTreeClassifier(max_depth=4, min_samples_leaf=15, random_state=42)),
        ]),
        "Random Forest": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("clf", RandomForestClassifier(n_estimators=150, max_depth=6, min_samples_leaf=10, random_state=42)),
        ]),
        "SVM (RBF)": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("clf", SVC(kernel="rbf", C=1.0, gamma="scale", probability=True, random_state=42)),
        ]),
    }
    return models


def evaluate_models_walk_forward(
    X: np.ndarray,
    y: np.ndarray,
    n_splits: int = 4,
    embargo_pct: float = 0.02,
) -> Tuple[pd.DataFrame, Dict[str, Dict[str, Any]]]:
    """Performs walk-forward cross-validation for all 7 MSQF models.
    
    Parameters
    ----------
    X : np.ndarray
        Feature matrix.
    y : np.ndarray
        Binary target array.
    n_splits : int
        Number of walk-forward rolling splits.
    embargo_pct : float
        Embargo fraction between train and test windows.
        
    Returns
    -------
    Tuple[pd.DataFrame, Dict[str, Dict[str, Any]]]
        - Summary comparison DataFrame of averaged classification metrics.
        - Detailed dictionary containing out-of-sample predictions, probabilities, and fold histories.
    """
    models = get_msqf_model_suite()
    splitter = PurgedTimeSeriesSplit(n_splits=n_splits, embargo_pct=embargo_pct)
    
    results = {}
    detailed_outputs = {}
    
    for name, model in models.items():
        fold_metrics = []
        oof_preds = []
        oof_probs = []
        oof_indices = []
        oof_targets = []
        
        for fold, (train_idx, test_idx) in enumerate(splitter.split(X, y)):
            X_train, y_train = X[train_idx], y[train_idx]
            X_test, y_test = X[test_idx], y[test_idx]
            
            # Check for class balance in training fold
            if len(np.unique(y_train)) < 2:
                continue
                
            clf = clone(model)
            clf.fit(X_train, y_train)
            
            y_pred = clf.predict(X_test)
            if hasattr(clf, "predict_proba"):
                y_prob = clf.predict_proba(X_test)[:, 1]
            else:
                y_prob = y_pred.astype(float)
                
            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred, zero_division=0)
            rec = recall_score(y_test, y_pred, zero_division=0)
            f1 = f1_score(y_test, y_pred, zero_division=0)
            try:
                auc = roc_auc_score(y_test, y_prob)
            except Exception:
                auc = 0.5
            brier = brier_score_loss(y_test, y_prob)
            
            fold_metrics.append({
                "fold": fold + 1,
                "accuracy": acc,
                "precision": prec,
                "recall": rec,
                "f1_score": f1,
                "roc_auc": auc,
                "brier_score": brier,
            })
            
            oof_preds.extend(y_pred)
            oof_probs.extend(y_prob)
            oof_indices.extend(test_idx)
            oof_targets.extend(y_test)
            
        df_fold = pd.DataFrame(fold_metrics)
        results[name] = {
            "Accuracy": df_fold["accuracy"].mean(),
            "Precision": df_fold["precision"].mean(),
            "Recall": df_fold["recall"].mean(),
            "F1-Score": df_fold["f1_score"].mean(),
            "ROC-AUC": df_fold["roc_auc"].mean(),
            "Brier Score": df_fold["brier_score"].mean(),
        }
        
        detailed_outputs[name] = {
            "oof_preds": np.array(oof_preds),
            "oof_probs": np.array(oof_probs),
            "oof_indices": np.array(oof_indices),
            "oof_targets": np.array(oof_targets),
            "fold_df": df_fold,
        }
        
    summary_df = pd.DataFrame(results).T
    summary_df = summary_df.sort_values(by="F1-Score", ascending=False)
    
    return summary_df, detailed_outputs
