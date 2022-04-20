import math

#talvez possua erro

#   INTEGRAIS
#           REGRA DOS TRAPEZIOS
# Entrada: funcao f, ponto a, ponto b, numPontosParticao

def double_trapezio(f, a:float, b:float, c:float, d:float, n1:int, n2:int) -> float:
   if n1 <= 0 or n2 <= 0:
      raise ValueError("Não pode")
   h1 = (b - a) / n1
   h2 = (d - c) / n2

   soma_interior = 0
   for i in range(1, n1):# N1 é a qtde de subintervalos
      for j in range(1, n2):
         soma_interior += f(a + i * h1, c + j * h2)

   soma_aresta_horizontal = 0
   for i in range(1 ,n1): # ignora o ponto 0 e ponto n1
      for j in [0, n2]: # só considera os pontos 0 e n2
         soma_aresta_horizontal += f(a + i * h1, c + j * h2)

   soma_aresta_vertical = 0
   for j in range(1 ,n2):
      for i in [0, n1]:
         soma_aresta_vertical += f(a + i * h1, c + j * h2)

   soma_vertice = 0
   for i in [0 ,n1]:
      for j in [0, n2]:
         soma_aresta_vertical += f(a + i * h1, c + j * h2)

   return (h1 * h2 / 4) * (soma_vertice + 4 * soma_interior + 2 * (soma_aresta_horizontal + soma_aresta_vertical))


def f(x,y):
   return math.exp(-x**2 - y ** 2)

if __name__ == "__main__":
   a,b = [1, 2]
   c,d = [-1, 0]
   n1, n2 = 5, 3
   print(double_trapezio(f, a, b, c, d, n1, n2))
