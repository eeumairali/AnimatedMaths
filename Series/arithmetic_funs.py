def arith_nth_term(a, n, d):
    return a+(n-1)*d
def arith_sum_of_nth_term(n, a1, a_n):
    return n/2*(a1+a_n)
def sum_expended(n, a1, d):
    return n/2*(2*a1+(n-1)*d)





if __name__ == "__main__":
    x = arith_nth_term(1,100,3) # 1 4 7 10
    print(x)

    print(arith_sum_of_nth_term(10, 1, 10)) # sum of 100 terms -> 14950
    print(sn(100, 1, 3))    # same -> 14950
