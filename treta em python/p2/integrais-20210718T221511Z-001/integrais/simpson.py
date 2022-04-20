
import math

#   INTEGRAIS
#           REGRA DE SIMPSON
# Entrada: funcao f, ponto a, ponto b, numSubIntervalosParticao

def simpson(f, a, b, n):
   if n % 2 != 0 or n < 1:
      raise ValueError("n deve ser par e maior que 1")
   h = (b - a) / n
   #  particao = [a + k * h for k in range(n + 1)]
   #  particao_impar = [a + k * h for k in range(1, n , 2)]
   #  particao_par = [a + k * h for k in range(1, n + 1, 2)]
   soma_impar, soma_par = 0, 0
   for k in range(1, n, 2): #Estamos considerand somente indice impar
      soma_impar += f(a + k * h)
   for k in range(2, n, 2): #Estamos considerand somente indice par
      soma_par += f(a + k * h)
   return (f(a) + 4 * soma_impar + 2 * soma_par + f(b)) * (h / 3)

def f(x):
   return math.exp(-x ** 2)

a,b = 0, 1
n = 10 #numero de subintervalos

if __name__ == "__main__":
   print(simpson(f, a, b, n))

