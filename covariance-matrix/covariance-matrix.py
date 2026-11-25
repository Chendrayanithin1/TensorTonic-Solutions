import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    X = np.array(X, dtype=float)   # always a fresh copy, safe to modify
    X -= X.mean(axis=0)            # centre in place, no extra array
    return X.T @ X / (X.shape[0] - 1)