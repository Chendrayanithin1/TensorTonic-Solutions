import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.asarray(A)
    if A.ndim != 2:
        raise ValueError(f"Expected a 2-D matrix, got {A.ndim}-D input")

    return A.T
