import math
import matplotlib.pyplot as plt
import numpy as np

def euler(f, x0, y0, h, n):
    r = []
    for i in range(n):
        #realizar iteracoes
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        yk = y0 + h * m2

        y0 = yk
        x0 += h
        r.append((x0, y0))
    return r

if __name__ == '__main__':

    def f(x, y):
        return y*(2-x)+x+1

    x0, y0 = 0.40582, 0.81397

    resposta = euler(f, x0, y0, h=0.10163, n=10)
    print(resposta)

    x, y = zip(*resposta)
    print(x)
    print(y)
    plt.scatter(x,y)
    plt.savefig('euler_half.png')
