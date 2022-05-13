import numpy as np


def f(x):
    return np.exp(np.cos(x)**2)+np.exp(-x**2)+np.log(x)


def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])


if __name__ == '__main__':
    x = [1.185 ,2.206, 3.365, 4.519, 5.52, 6.273, 7.288,8.679]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)
    print(abs(f(0.327) - p(0.327, coefs)))
    print(abs(f(1.765 ) - p(1.765 , coefs)))
    print(abs(f(2.811) - p(2.811, coefs))) #pontos