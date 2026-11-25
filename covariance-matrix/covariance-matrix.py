import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Sample covariance matrix of X, where rows are observations
    and columns are variables. Returns a (d, d) NumPy array.
    """
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X[:, None]           
    n = X.shape[0]
    if n < 2:
        raise ValueError("need at least 2 observations")

    Xc = X - X.mean(axis=0)      
    return Xc.T @ Xc / (n - 1)