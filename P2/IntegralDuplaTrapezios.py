import math

def double_trapz(f, a:float, b:float, c:float ,d:float, n1:int, n2:int) -> float:
    h1 = (b - a) / n1
    h2 = (d - c) / n2

    soma_interior = 0
    for i in range(1, n1):
        for j in range(1, n2):
            soma_interior += f(a + i * h1, c + j * h2)

    soma_arestas_horizontais = 0
    for i in range(1, n1):
        for j in [0,n2]:
            soma_arestas_horizontais += f(a + i * h1, c + j * h2)

    soma_arestas_verticais = 0
    for j in range(1, n2):
        for i in [0,n1]:
            soma_arestas_verticais += f(a + i * h1, c + j * h2)
    
    soma_vertices = 0
    for i in [0, n1]:
        for j in [0,n2]:
            soma_vertices += f(a + i * h1, c + j * h2)

    return (h1 * h2 / 4) * (soma_vertices + 4 * soma_interior + 2 * (soma_arestas_horizontais + soma_arestas_verticais))

def f(x, y):
    return math.sqrt(math.exp(-x**2*y**2)+1)

a, b = [-1.898, 1.309]
c, d = [-1.996, 1.22]
n1, n2 = 10,21

print(double_trapz(f, a, b, c, d, n1, n2))