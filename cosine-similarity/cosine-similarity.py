import numpy as np
import math
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    if a.ndim != 1 or b.ndim !=1:
        raise ValueError("Both inputs should be 1-D Vectors")
    if a.shape != b.shape:
        raise ValueError(f"Length mismatch: {a.size} vd {b.size}")
    denom =  math.sqrt(float(a@a) * float(b@b))

    if denom==0.0:
        return 0.0
    return max(-1.0, min(1.0, float(a@b)/denom))