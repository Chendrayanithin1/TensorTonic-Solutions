from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.asarray(x, dtype= float)

    value , count = np.unique(x, return_counts =True)
    mode_val = value[np.argmax(count)]
    return {"mean":float(np.mean(x)), "median": float(np.median(x)), "mode":float(mode_val)}