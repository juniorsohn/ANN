
import math

#   INTEGRAIS
#           REGRA DOS TRAPEZIOS
# Entrada: funcao f, ponto a, ponto b, numPontosParticao

def trapezio(f, a, b, n):
   h = (b - a) / n
   soma = 0
   for k in range(1,n):#comecar em 1 evitando que o primeiro ponto seja calculado 2 vezes
      soma += f(a + k * h)
   soma *= 2
   soma += (f(a) + f(b))
   soma *= (h / 2)
   return soma

def f(x):
   return math.exp(-x**2)

if __name__ == "__main__":
   a,b = 0, 1
   n = 5
   print(trapezio(f,a,b,n))
