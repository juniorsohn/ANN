
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
   for k in range(1, n, 2): #Estamos considerando somente indice impar
      soma_impar += f(a + k * h)
   for k in range(2, n, 2): #Estamos considerando somente indice par
      soma_par += f(a + k * h)
   return (f(a) + 4 * soma_impar + 2 * soma_par + f(b)) * (h / 3)

def f(x):
   return math.exp(-x ** 2)

a,b = [-0.637, 0.662]
n = 10 #numero de subintervalos
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 56
# def f(x):
#    return math.e**(-x**2)
# a,b = [-0.637, 0.662]
#subintervalos = [4, 24, 40, 52, 76, 118, 212, 392, 610, 772, 1056]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 5-
x = [0.004, 0.072, 0.14, 0.3425, 0.545, 0.5485, 0.552, 0.614, 0.676, 0.777, 0.878, 0.93, 0.982, 1.038, 1.094, 1.317, 1.54, 1.8765, 2.213, 2.234, 2.255, 2.7175, 3.18, 3.2265, 3.273, 3.2915, 3.31, 3.3535, 3.397, 3.4875, 3.578, 3.6295, 3.681, 3.796, 3.911, 4.0165, 4.122, 4.172, 4.222, 4.5665, 4.911]
y = [1.254, 1.456, 1.687, 2.384, 2.854, 2.86, 2.865, 2.939, 2.983, 2.997, 2.952, 2.911, 2.861, 2.799, 2.732, 2.45, 2.21, 2.015, 2.045, 2.055, 2.065, 2.492, 2.984, 2.998, 2.999, 2.995, 2.989, 2.966, 2.928, 2.801, 2.606, 2.467, 2.311, 1.916, 1.512, 1.202, 1.022, 1.0, 1.025, 2.299, 2.814]

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX P2.7
x = [0.888, 0.9055, 0.923, 1.2705, 1.618, 1.831, 2.044, 2.5905, 3.137]
y = [2.945, 2.931, 2.917, 2.507, 2.145, 2.029, 2.002, 2.342, 2.962]
#--------------------------------------------------------------------------


if __name__ == "__main__":
   #print(simpson(f, a, b, n)) #simples
   #for i in range(len(subintervalos)):#57
      #print(subintervalos[i],simpson(f,a,b,subintervalos[i]))
   #   print(simpson(f,a,b,subintervalos[i]))#57
   sum = 0.0
   for n in range(2,len(x),2):
      sum += ((x[n-1] - x[n-2])/3) * (y[n-2] + 4*y[n-1] + y[n])
      #print('{} -- ({},{})'.format(i,x[i],y[i]))
   print(sum)

