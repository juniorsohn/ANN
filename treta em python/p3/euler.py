import math
import matplotlib.pyplot as plt
import numpy as np

def euler(f, x0, y0, h, n):
    result = []
    for i in range(n):
        y0 += f(x0, y0) * h
        x0 += h
        result.append([x0, y0])
        print(x0,y0)
        # print(f'x_{i+1} = {x0} \t||\t y_{i+1} = {y0}')
    return result

if __name__ == '__main__':

    # def f(x, y):
    #     return y*(1 - x) + x + 2

    # x0, y0 = 1.72962, 1.56925
    # h = 0.18607
    # n = 10

    #P3.7
    def f(x, y):
        return y*(1 - x) + x + 2

    x0, y0 = 1.38244, 1.39293
    h = 0.17772
    n = 10

    resposta = euler(f, x0, y0, h, n)

    def y(x):
        return 5 * math.exp(x - 1) - x - 2

    t = np.linspace(x0, x0 + n * h, 100)
    yt = [y(i) for i in t]

    cx, cy = zip(*resposta)
    plt.plot(t, yt)
    plt.scatter(cx, cy)
    plt.savefig('euler.png')
