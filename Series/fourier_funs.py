import math


def fourier_series(a0, an, bn, x):
    total = a0 / 2
    terms = min(len(an), len(bn))

    for n in range(1, terms + 1):
        total += an[n - 1] * math.cos(n * x) + bn[n - 1] * math.sin(n * x)

    return total


def _integrate_over_period(function, integrand, steps=2000):
    step = (2 * math.pi) / steps
    total = 0.0

    for index in range(steps):
        x = -math.pi + index * step
        total += function(x) * integrand(x)

    return total * step


def fourier_cosine_coefficient(function, n, steps=2000):
    return _integrate_over_period(function, lambda x: math.cos(n * x), steps) / math.pi


def fourier_sine_coefficient(function, n, steps=2000):
    return _integrate_over_period(function, lambda x: math.sin(n * x), steps) / math.pi


if __name__=="__main__":
    a0 = 1
    an = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x = math.pi / 4

    print(fourier_series(a0, an, bn, x))
    

        