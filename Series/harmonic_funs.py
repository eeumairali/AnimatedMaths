from math import log as ln
def harmonic_num(n, k):
    try:
        n = int(float(n))
        k = float(k)
    except (TypeError, ValueError):
        return "Error, n and k must be numeric"

    if n <= 0:
        return "Error, n must be greater than 0"
    harm_sum = 0
    for i in range(1, n + 1):
        harm_sum += 1 / (i ** k) 
    return harm_sum

def harominic_nth_term(a1,n,d):
    output = a1 + (n-1)*d
    if output == 0:
        return "Error, denominator cannot be 0"
    return 1/output

def asym_aprox(n,lbda):
    return ln(n) + lbda