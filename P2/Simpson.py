# requer número impar de pontos
import math

def simps(f, a, b, n):
    h = (b - a) / n
    soma_impar = sum([f(a + k * h) for k in range(1, n , 2)])
    soma_par   = sum([f(a + k * h) for k in range(2, n , 2)])
    return (h/3) * (f(a) + 4 * soma_impar + 2 * soma_par + f(b))

def f(x):
    return math.exp(-x**2)

# a, b = 0, 1
# n = 10 # nro de subintervalos, n/2 é o nro de parabolas, n+1 é o nro de pontos na partição
# i1 = simps(f, a, b, n)
# print(i1)

def g(x):
    return math.cos(x ** 2)

x = [0.326, 0.664, 1.002, 1.1045, 1.207, 1.3195, 1.432, 1.433, 1.434, 2.0115, 2.589, 2.597, 2.605, 2.724, 2.843, 2.9935, 3.144, 3.5065, 3.869, 3.8725, 3.876, 4.1565, 4.437]
y = [2.333, 2.977, 2.839, 2.719, 2.588, 2.447, 2.317, 2.316, 2.315, 2.0, 2.34, 2.349, 2.358, 2.5, 2.652, 2.834, 2.966, 2.766, 1.656, 1.643, 1.631, 1.002, 1.663]
soma = 0
xy = zip(x,y)

for n in range(2,len(x),2): # lista de x e y removidos os primeiros elementos
    # print(n, x[n-2], x[n-1], x[n])
    soma += ((x[n-1] - x[n-2])/3) * (y[n-2] + 4*y[n-1] + y[n])

print(soma)