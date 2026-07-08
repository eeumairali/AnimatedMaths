def geo_nth_term(a1,r,n):
    return a1 * r ** (n-1)
def geo_sum_nth_terms(a1, r, n):
    return a1*((1-r**n)/(1-r))

def geo_infinity_sum(a1,r):
    if abs(r)<1:
        return (a1/(1-r))
    return "Error, value is undefined"
        


if __name__ == "__main__":
    # 1 4 16 64 . . . 7th
    print(geo_nth_term(1,4,8))
    