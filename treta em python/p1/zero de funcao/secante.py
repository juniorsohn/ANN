import math

####--####--####--####--####--##
#Exercise 15

# def f(x):
#   return x**2 -4*x +2 -numpy.log(x)

# x0 = 1.24925
# x1 = 4.17842
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 16

# def f(x):
#   return x -2**-x

# x0 = 0.09354
# x1 = 1.41724
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 17

# def f(x):
#   return x**2 - 5

# x0 = 1.68311
# x1 = 2.57454
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 18

# def f(x):
#   return math.sqrt(x) - math.cos(x)
# x0 = 0.49285
# x1 = 1.29871
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 19

# def f(x):
#   return math.pi*x - math.e**x
# x0 = 1.00814
# x1 = 2.10317
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 20

# def f(x):
#   return math.e**x - 2*x**2 + x - 1.5
# x0 = 0.17496
# x1 = 2.48024
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 21

# def f(x):
#   return x**2 - 3
# x0 = -2.23289
# x1 = -0.65706
# numIteracao = 5
####--####--####--####--####--##
###--####--####--####--####--##
# PROVA - 3

def f(x):
    
    g = 9.81
    c = 18.22
    v = 39.61
    t = 8.2

    return ((g*x)/c) * (1 - math.e**(-(c/x)*t)) - v

x0= 26.95
x1= 38.94
numIteracao = 5

###--####--####--####--####--##

#   ZERO DE FUNCAO
#           METODO DA SECANTE
# Entrada: estimativa inicial (x0), estimativa inicial (x1), funcao (f) numero de iteracoes (numIteracao)
def metodoSecante(x0, x1, f, numIteracao):
  print("Calcular metodo da secante !!\n\n")
  for i in range(numIteracao):
    if (f(x1) - f(x0) == 0):
      print("Divisao por zero na derivada em {}\n".format(x0))
      break
    x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
    print("x_{} = {}\n".format(i + 1,x2))
    x0 = x1
    x1 = x2

if __name__ == "__main__":
  metodoSecante(x0, x1, f, 1)
  print("-")
  metodoSecante(x0, x1, f, 4)
  print("-")
  metodoSecante(x0, x1, f, 5)