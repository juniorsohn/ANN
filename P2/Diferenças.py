import matplotlib.pyplot as plt
import numpy as np
import math

def diferencas(x,y):
    Y = [x for x in y] # copiando y em Y para não alterar a lista original
    n = len(y)
    coeficientes = [y[0]] + [0] *(n-1)
    for i in range(n-1): # colunas
        for j in range(n-1-i): # linhas
            numerador   = Y[j+1] - Y[j]
            denominador = x[j+1+i] - x[j]
            Y[j] = numerador / denominador
        coeficientes[i+1] = Y[0]
    return coeficientes

def equacao(x, coeficientes): # constroi a equação do polinomio interpolador
    n = len(x)
    polinomio = ''
    for i in range(n):
        sign = '*' if i!= 0 else ''
        polinomio += f'{coeficientes[i]:+}{sign}'+'*'.join([f'(x{-xj:+})' for j,xj in enumerate(x) if j < i])

    return polinomio

def f(x):
    return (math.cos(x)**3)+ 2*math.cos(x)**2+1 

x = [-2.895, -1.723, -1.55, -0.552, 0.315, 0.855, 1.579, 2.07, 2.878, 3.715, 4.215]
y = [f(xi) for xi in x]

coeficientes = diferencas(x,y)
# polinomio = equacao(x,coeficientes)
for x in coeficientes:
    print(x)
# coeficientes = diferencas(x,y)
# polinomio = equacao(x,coeficientes)
# print(coeficientes)
# print(polinomio)

# t = np.linspace(min(x), max(x), 100)

# def p(x):
#     return eval(polinomio)

# plt.plot(t, p(t))
# plt.scatter(x,y, zorder=10)
# plt.savefig("diferenças.png")