import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    def x(i):
        return math.comb(n,i)*((p**i)*((1-p)**(n-i)))
    pmf = float(x(k))
    cdf = 0
    for i in range(0,k+1):
        cdf = cdf + x(i)

    return {'pmf': pmf,'cdf' : float(cdf)}