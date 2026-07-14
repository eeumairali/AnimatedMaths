mult=0
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)


def taylor_exponential(x):
    total = 0
    for n in range(10):
        total+=(x**n)/fact(n)
    return total

def taylor_sine(x):
    total = 0
    for n in range(10):
        total+=((-1)**n)*(x**(2*n+1))/fact(2*n+1)
    return total

def degree2Radian(degree):
    return degree*3.14159/180

def taylor_cosine(x):
    total = 0
    for n in range(10):
        total+=((-1)**n)*(x**(2*n))/fact(2*n)
    return total

if __name__=="__main__":
    print(taylor_sine(degree2Radian(270)))
    print(taylor_cosine(degree2Radian(270)))