"""
==============================================================================
MSQF 536: MACHINE LEARNING TECHNIQUES - UNIT I ASSIGNMENT CODE
Data Pre-processing Practical Solutions & Python Exercises
Department of Statistics, Pondicherry University
Student Name: N Rohit Vedhanandh
==============================================================================
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification


# ==============================================================================
# SECTION D: PYTHON EXERCISES
# ==============================================================================

print("=" * 80)
print("SECTION D: PYTHON EXERCISES")
print("=" * 80)

# ------------------------------------------------------------------------------
# Exercise 1: Identifying Variable Types
# ------------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Exercise 1: Identifying Variable Types")
print("-" * 60)

data_ex1 = {
    'stock': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'],
    'sector': ['Technology', 'Technology', 'Technology', 'E-commerce', 'Automotive'],
    'credit_rating': ['AA', 'AAA', 'AA+', 'A+', 'BBB+'],
    'close_price': [175.34, 140.56, 330.45, 165.23, 245.67],
    'num_trades': [1500, 1200, 980, 2100, 1650]
}

df_ex1 = pd.DataFrame(data_ex1)

print("1) DataFrame:")
print(df_ex1)
print("\n2) Data Types:")
print(df_ex1.dtypes)

categorical_cols = df_ex1.select_dtypes(include=['object']).columns.tolist()
print("\n3) Categorical Variables:", categorical_cols)

numerical_cols = df_ex1.select_dtypes(include=['int64', 'float64']).columns.tolist()
print("4) Numerical Variables:", numerical_cols)


# ------------------------------------------------------------------------------
# Exercise 2: Scaling and Encoding
# ------------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Exercise 2: Scaling and Encoding")
print("-" * 60)

data_ex2 = {
    'close_price': [100, 250, 150, 300, 200, 50, 180, 400],
    'sector': ['Banking', 'IT', 'IT', 'Pharma', 'Banking', 'IT', 'Pharma', 'Banking']
}

df_ex2 = pd.DataFrame(data_ex2)
print("Original DataFrame:")
print(df_ex2)

scaler_minmax = MinMaxScaler()
df_ex2['close_price_minmax'] = scaler_minmax.fit_transform(df_ex2[['close_price']])

scaler_std = StandardScaler()
df_ex2['close_price_zscore'] = scaler_std.fit_transform(df_ex2[['close_price']])
print("\nAfter Scaling:")
print(df_ex2)

one_hot = pd.get_dummies(df_ex2['sector'], prefix='sector')
df_encoded = pd.concat([df_ex2, one_hot], axis=1)
df_encoded = df_encoded.drop('sector', axis=1)
print("\nAfter One-Hot Encoding:")
print(df_encoded)


# ------------------------------------------------------------------------------
# Exercise 3: Missing-Value Imputation
# ------------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Exercise 3: Missing-Value Imputation")
print("-" * 60)

np.random.seed(42)
data_ex3 = {
    'stock_price': [100, np.nan, 150, 200, np.nan, 180, 220, 160, 190, np.nan],
    'trading_volume': [1000, 1200, np.nan, 1500, 1300, np.nan, 1100, 1400, 1600, 1700],
    'return_ratio': [0.05, 0.03, 0.08, np.nan, 0.02, 0.07, 0.04, 0.06, np.nan, 0.09]
}

df_ex3 = pd.DataFrame(data_ex3)
print("Original DataFrame with Missing Values:")
print(df_ex3)

print("\nMissing Values per Column:")
print(df_ex3.isnull().sum())

df_mean = df_ex3.copy()
df_mean['stock_price'] = df_mean['stock_price'].fillna(df_mean['stock_price'].mean())
df_mean['trading_volume'] = df_mean['trading_volume'].fillna(df_mean['trading_volume'].mean())
df_mean['return_ratio'] = df_mean['return_ratio'].fillna(df_mean['return_ratio'].mean())
print("\nMean Imputation:")
print(df_mean)

df_median = df_ex3.copy()
df_median['stock_price'] = df_median['stock_price'].fillna(df_median['stock_price'].median())
df_median['trading_volume'] = df_median['trading_volume'].fillna(df_median['trading_volume'].median())
df_median['return_ratio'] = df_median['return_ratio'].fillna(df_median['return_ratio'].median())
print("\nMedian Imputation:")
print(df_median)

knn_imputer = KNNImputer(n_neighbors=2)
df_knn = pd.DataFrame(knn_imputer.fit_transform(df_ex3), columns=df_ex3.columns)
print("\nKNN Imputation:")
print(df_knn)

print("\nComparison of Imputation Methods (Stock Price):")
print(f"Original missing values: {df_ex3['stock_price'].isnull().sum()}")
print(f"Mean imputation values:   {df_mean['stock_price'].tolist()}")
print(f"Median imputation values: {df_median['stock_price'].tolist()}")
print(f"KNN imputation values:    {df_knn['stock_price'].tolist()}")


# ------------------------------------------------------------------------------
# Exercise 4: Train-Test Split
# ------------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Exercise 4: Train-Test Split")
print("-" * 60)

np.random.seed(42)
n_samples = 1000
data_ex4 = {
    'feature1': np.random.randn(n_samples),
    'feature2': np.random.randn(n_samples),
    'feature3': np.random.randn(n_samples),
    'target': np.random.randint(0, 2, n_samples)
}
df_ex4 = pd.DataFrame(data_ex4)

print(f"Original dataset observations: {len(df_ex4)}")
print(f"Original dataset shape: {df_ex4.shape}")

X_ex4 = df_ex4.drop('target', axis=1)
y_ex4 = df_ex4['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_ex4, y_ex4, 
    test_size=0.2,
    random_state=42,
    stratify=y_ex4
)

print(f"Training set observations: {len(X_train)}")
print(f"Testing set observations:  {len(X_test)}")


# ------------------------------------------------------------------------------
# Exercise 5: Class Imbalance
# ------------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Exercise 5: Class Imbalance")
print("-" * 60)

X_raw, y_raw = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=10,
    n_redundant=5,
    n_classes=2,
    weights=[0.9, 0.1],
    random_state=42
)
df_raw = pd.DataFrame(X_raw)
df_raw['target'] = y_raw

print("Class Distribution BEFORE Balancing:")
print(df_raw['target'].value_counts())
print(f"Class 0: {df_raw['target'].value_counts()[0]} ({df_raw['target'].value_counts()[0]/len(df_raw)*100:.2f}%)")
print(f"Class 1: {df_raw['target'].value_counts()[1]} ({df_raw['target'].value_counts()[1]/len(df_raw)*100:.2f}%)")

try:
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_raw, y_raw)
except ImportError:
    from sklearn.neighbors import NearestNeighbors
    min_idx = np.where(y_raw == 1)[0]
    maj_idx = np.where(y_raw == 0)[0]
    X_min = X_raw[min_idx]
    n_to_sample = len(maj_idx) - len(min_idx)
    nn = NearestNeighbors(n_neighbors=5).fit(X_min)
    knns = nn.kneighbors(X_min, return_distance=False)
    synth = []
    for _ in range(n_to_sample):
        i = np.random.randint(0, len(X_min))
        neighbor_idx = knns[i, np.random.randint(1, 5)]
        diff = X_min[neighbor_idx] - X_min[i]
        synth.append(X_min[i] + np.random.rand() * diff)
    X_resampled = np.vstack([X_raw, np.array(synth)])
    y_resampled = np.hstack([y_raw, np.ones(n_to_sample, dtype=int)])

df_balanced = pd.DataFrame(X_resampled)
df_balanced['target'] = y_resampled

print("\nClass Distribution AFTER Balancing:")
print(df_balanced['target'].value_counts())
print(f"Class 0: {df_balanced['target'].value_counts()[0]} ({df_balanced['target'].value_counts()[0]/len(df_balanced)*100:.2f}%)")
print(f"Class 1: {df_balanced['target'].value_counts()[1]} ({df_balanced['target'].value_counts()[1]/len(df_balanced)*100:.2f}%)")

print("\nComparison of Class Distributions:")
print(f"{'Metric':<20} {'Before':<15} {'After':<15}")
print("-" * 50)
print(f"{'Total samples':<20} {len(df_raw):<15} {len(df_balanced):<15}")
print(f"{'Minority class':<20} {df_raw['target'].value_counts()[1]:<15} {df_balanced['target'].value_counts()[1]:<15}")
print(f"{'Majority class':<20} {df_raw['target'].value_counts()[0]:<15} {df_balanced['target'].value_counts()[0]:<15}")
print(f"{'Imbalance ratio':<20} {df_raw['target'].value_counts()[0]/df_raw['target'].value_counts()[1]:<15.2f} {df_balanced['target'].value_counts()[0]/df_balanced['target'].value_counts()[1]:<15.2f}")


# ==============================================================================
# SECTION E: FINANCE CASE STUDY (LOAN DEFAULT PREDICTION WORKFLOW)
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION E: LOAN DEFAULT PREDICTION PRE-PROCESSING WORKFLOW")
print("=" * 80)

# Generate synthetic historical credit dataset
np.random.seed(42)
n_records = 500

raw_loan_data = {
    'Age': np.random.choice([25, 30, 45, np.nan, 50, 35, 60, 28], size=n_records),
    'Income': np.random.choice([45000, 65000, 120000, np.nan, 85000, 95000], size=n_records),
    'Credit_Score': np.random.choice([650, 720, 580, 800, np.nan, 690, 740], size=n_records),
    'Employment_Type': np.random.choice(['Salaried', 'Self-Employed', 'Business', np.nan], size=n_records),
    'Credit_Rating': np.random.choice(['AAA', 'AA', 'A', 'BBB', 'BBB+', 'A+', np.nan], size=n_records),
    'Loan_Amount': np.random.choice([10000, 25000, 50000, np.nan, 15000, 35000], size=n_records),
    'Debt_to_Income_Ratio': np.random.choice([0.25, 0.35, 0.45, np.nan, 0.20, 0.50], size=n_records),
    'Previous_Default': np.random.choice([0, 1], p=[0.85, 0.15], size=n_records),
    'Loan_Default': np.random.choice([0, 1], p=[0.90, 0.10], size=n_records)
}

df_loan = pd.DataFrame(raw_loan_data)
df_loan.to_csv('loan_data.csv', index=False)

# Step 1: Load and Explore Data
df = pd.read_csv('loan_data.csv')
print("Step 1: Dataset shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

# Step 2: Separate Features and Target
X = df.drop('Loan_Default', axis=1)
y = df['Loan_Default']

# Step 3: Identify Variable Types
num_cols = ['Age', 'Income', 'Credit_Score', 'Loan_Amount', 'Debt_to_Income_Ratio']
cat_cols = ['Employment_Type', 'Credit_Rating']
bin_cols = ['Previous_Default']

# Step 4: Train-Validation-Test Split (70-15-15)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
)

# Step 5: Handle Missing Values - Numerical
num_imputer = SimpleImputer(strategy='median')
X_train_num = num_imputer.fit_transform(X_train[num_cols])
X_val_num = num_imputer.transform(X_val[num_cols])
X_test_num = num_imputer.transform(X_test[num_cols])

# Step 6: Handle Missing Values - Categorical
cat_imputer = SimpleImputer(strategy='most_frequent')
X_train_cat = cat_imputer.fit_transform(X_train[cat_cols])
X_val_cat = cat_imputer.transform(X_val[cat_cols])
X_test_cat = cat_imputer.transform(X_test[cat_cols])

# Step 7: Scale Numerical Variables
scaler = StandardScaler()
X_train_num_scaled = scaler.fit_transform(X_train_num)
X_val_num_scaled = scaler.transform(X_val_num)
X_test_num_scaled = scaler.transform(X_test_num)

# Step 8: Encode Categorical Variables
rating_order = ['BBB', 'BBB+', 'A-', 'A', 'A+', 'AA-', 'AA', 'AA+', 'AAA']
ord_encoder = OrdinalEncoder(categories=[rating_order], handle_unknown='use_encoded_value', unknown_value=-1)
X_train_rating = ord_encoder.fit_transform(X_train_cat[:, 1].reshape(-1, 1))
X_val_rating = ord_encoder.transform(X_val_cat[:, 1].reshape(-1, 1))
X_test_rating = ord_encoder.transform(X_test_cat[:, 1].reshape(-1, 1))

one_hot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_train_employment = one_hot_encoder.fit_transform(X_train_cat[:, 0].reshape(-1, 1))
X_val_employment = one_hot_encoder.transform(X_val_cat[:, 0].reshape(-1, 1))
X_test_employment = one_hot_encoder.transform(X_test_cat[:, 0].reshape(-1, 1))

# Step 9: Combine Features
X_train_processed = np.hstack([
    X_train_num_scaled,
    X_train_employment,
    X_train_rating,
    X_train[bin_cols].to_numpy()
])
X_val_processed = np.hstack([
    X_val_num_scaled,
    X_val_employment,
    X_val_rating,
    X_val[bin_cols].to_numpy()
])
X_test_processed = np.hstack([
    X_test_num_scaled,
    X_test_employment,
    X_test_rating,
    X_test[bin_cols].to_numpy()
])

# Step 10: Handle Class Imbalance (only on training data)
try:
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train_processed, y_train)
except ImportError:
    pos_mask = (y_train == 1)
    pos_samples = X_train_processed[pos_mask]
    n_add = (y_train == 0).sum() - (y_train == 1).sum()
    add_indices = np.random.choice(len(pos_samples), size=n_add, replace=True)
    X_train_balanced = np.vstack([X_train_processed, pos_samples[add_indices]])
    y_train_balanced = np.hstack([y_train, np.ones(n_add, dtype=int)])

# Step 11: Save Preprocessed Data
np.save('X_train_balanced.npy', X_train_balanced)
np.save('y_train_balanced.npy', y_train_balanced)
np.save('X_val_processed.npy', X_val_processed)
np.save('y_val.npy', y_val)
np.save('X_test_processed.npy', X_test_processed)
np.save('y_test.npy', y_test)

# Step 12: Verify and Document
print("\nPreprocessing Complete!")
print(f"Training set shape:   {X_train_balanced.shape}")
print(f"Validation set shape: {X_val_processed.shape}")
print(f"Test set shape:       {X_test_processed.shape}")
print(f"Class distribution after SMOTE: {np.unique(y_train_balanced, return_counts=True)}")
print("\nAll tasks completed successfully!")
