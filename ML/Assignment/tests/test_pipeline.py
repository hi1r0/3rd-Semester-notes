"""
test_pipeline.py
================
Automated Sanity and Unit Tests for the ML Pair Trading Framework.
"""

import unittest
import numpy as np
import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.simulation import simulate_pair, simulate_multi_pair_universe
from src.cointegration import compute_spread_and_zscore
from src.features import extract_signal_features
from src.labeling import apply_triple_barrier_labeling
from src.models import get_msqf_model_suite, PurgedTimeSeriesSplit, evaluate_models_walk_forward
from src.backtest import evaluate_trading_performance, run_strategy_backtests


class TestPairTradingMLPipeline(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Load real market dataset across pairs
        cls.universe = simulate_multi_pair_universe()
        cls.test_df = cls.universe["XOM_CVX"]
        cls.cointeg_df = compute_spread_and_zscore(cls.test_df, ols_window=60, z_window=30)
        cls.feat_df = extract_signal_features(cls.cointeg_df, lookback=40)
        cls.labeled_df = apply_triple_barrier_labeling(
            df=cls.cointeg_df,
            features_df=cls.feat_df,
            horizon=12,
            exit_z=0.0,
            stop_z=3.5,
            transaction_cost=0.0010,
        )

    def test_market_data(self):
        """Verify real market data loads all 5 equity and ETF pairs without NaNs."""
        self.assertEqual(len(self.universe), 5)
        expected_pairs = ["KO_PEP", "XOM_CVX", "JPM_BAC", "BP_SHEL", "GLD_SPY"]
        for p_id in expected_pairs:
            self.assertIn(p_id, self.universe)
            df = self.universe[p_id]
            self.assertGreater(len(df), 1000)
            self.assertTrue((df["price_x"] > 0).all())
            self.assertTrue((df["price_y"] > 0).all())
            self.assertFalse(df["true_spread"].isna().any())

    def test_cointegration_and_zscore(self):
        """Verify rolling cointegration and signal triggers."""
        self.assertIn("z_score", self.cointeg_df.columns)
        self.assertIn("is_entry", self.cointeg_df.columns)
        n_entries = self.cointeg_df["is_entry"].sum()
        self.assertGreater(n_entries, 0, "No candidate entry triggers were generated.")

    def test_feature_engineering(self):
        """Verify feature extraction produces all 12 quantitative features."""
        required_features = [
            "z_score", "spread_momentum_1d", "spread_momentum_5d", "spread_momentum_10d",
            "ou_half_life", "hurst_exponent", "adf_pvalue", "autocorr_lag1", "autocorr_lag2",
            "volatility_ratio", "rolling_correlation", "hedge_ratio_stability",
        ]
        self.assertGreater(len(self.feat_df), 0)
        for col in required_features:
            self.assertIn(col, self.feat_df.columns)
            self.assertFalse(self.feat_df[col].isna().any(), f"Feature {col} contains NaNs.")
            self.assertTrue(np.isfinite(self.feat_df[col].to_numpy()).all(), f"Feature {col} contains non-finite values.")

    def test_meta_labeling(self):
        """Verify triple barrier labeling produces valid binary targets and returns."""
        self.assertGreater(len(self.labeled_df), 0)
        self.assertIn("target", self.labeled_df.columns)
        self.assertIn("net_return", self.labeled_df.columns)
        unique_targets = set(self.labeled_df["target"].unique())
        self.assertTrue(unique_targets.issubset({0, 1}))
        # Check holding periods within horizon
        self.assertTrue((self.labeled_df["holding_period"] <= 12).all())

    def test_msqf_model_suite(self):
        """Verify all 7 MSQF curriculum models instantiate and train."""
        models = get_msqf_model_suite()
        self.assertEqual(len(models), 7)
        expected_names = [
            "Logistic Regression", "Naive Bayes", "KNN", "Decision Tree",
            "Random Forest", "SVM (RBF)", "MLP (Neural Net)"
        ]
        for name in expected_names:
            self.assertIn(name, models)

    def test_walk_forward_evaluation_and_backtest(self):
        """Verify walk-forward evaluation and comparative backtesting."""
        feature_cols = [
            "z_score", "spread_momentum_1d", "spread_momentum_5d", "spread_momentum_10d",
            "ou_half_life", "hurst_exponent", "adf_pvalue", "autocorr_lag1", "autocorr_lag2",
            "volatility_ratio", "rolling_correlation", "hedge_ratio_stability",
        ]
        X = self.labeled_df[feature_cols].to_numpy()
        y = self.labeled_df["target"].to_numpy()
        
        # Test Purged split
        summary_df, detailed_outputs = evaluate_models_walk_forward(X, y, n_splits=3, embargo_pct=0.03)
        self.assertEqual(len(summary_df), 7)
        self.assertIn("F1-Score", summary_df.columns)
        self.assertIn("ROC-AUC", summary_df.columns)
        
        # Test Backtest
        comp_df, equity_curves = run_strategy_backtests(self.labeled_df, detailed_outputs, prob_threshold=0.50)
        self.assertIn("Traditional (No ML)", comp_df.index)
        self.assertIn("ML: Random Forest", comp_df.index)
        self.assertIn("Sharpe Ratio", comp_df.columns)
        self.assertIn("Max Drawdown (%)", comp_df.columns)

    def test_visualizations(self):
        """Verify that visualization routines generate figures without errors."""
        import matplotlib.pyplot as plt
        from src.visualization import (
            plot_market_regimes,
            plot_zscore_and_signals,
            plot_roc_curves,
            plot_feature_importance,
            plot_equity_and_drawdown,
        )
        
        fig1 = plot_market_regimes(self.universe)
        self.assertIsNotNone(fig1)
        plt.close(fig1)
        
        fig2 = plot_zscore_and_signals(self.cointeg_df, max_bars=300)
        self.assertIsNotNone(fig2)
        plt.close(fig2)
        
        # Test mock ROC and Equity
        feature_cols = [
            "z_score", "spread_momentum_1d", "spread_momentum_5d", "spread_momentum_10d",
            "ou_half_life", "hurst_exponent", "adf_pvalue", "autocorr_lag1", "autocorr_lag2",
            "volatility_ratio", "rolling_correlation", "hedge_ratio_stability",
        ]
        X = self.labeled_df[feature_cols].to_numpy()
        y = self.labeled_df["target"].to_numpy()
        _, detailed_outputs = evaluate_models_walk_forward(X, y, n_splits=2, embargo_pct=0.03)
        
        fig3 = plot_roc_curves(detailed_outputs)
        self.assertIsNotNone(fig3)
        plt.close(fig3)
        
        dummy_importances = np.linspace(0.01, 0.25, len(feature_cols))
        fig4 = plot_feature_importance(feature_cols, dummy_importances)
        self.assertIsNotNone(fig4)
        plt.close(fig4)
        
        _, equity_curves = run_strategy_backtests(self.labeled_df, detailed_outputs)
        fig5 = plot_equity_and_drawdown(equity_curves)
        self.assertIsNotNone(fig5)
        plt.close(fig5)


if __name__ == "__main__":
    unittest.main()
