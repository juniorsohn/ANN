import math
from tkinter import S

from numpy import mat

####--####--####--####--####--##
# #Exercise 8
#def f(x):
#   return math.e**(5*x) - 2

#def df(x):
#   return 5*math.e**(5*x)

# x0 = 0.57934
# numIteracao = 10
####--####--####--####--####--##
####--####--####--####--####--##
# #Exercise 9
#def f(x):
#   return math.pi*x - math.e**x

#def df(x):
#   return math.pi - math.e**x

# x0 = 2.19082
# numIteracao = 5
####--####--####--####--####--##
# #Exercise 10

# def f(x):
#   return 2*(x+1)*(x-1/2)*(x-1)

# def df(x):
#   return 6*x**2 - 2*x - 2

# x0 = 0.07678
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 11

# def f(x):
#   return x**3 - 7*x**2 + 14*x - 7

# def df(x):
#   return 3*x**2 -14*x + 14

# x0 = 0.27116
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 12

#def f(x):
#   return math.sqrt(x) - math.cos(x)

#def df(x):
#   return 1/(2*math.sqrt(x)) + math.sin(x)

# x0 = 0.2407
# numIteracao = 5
####--####--####--####--####--##

####--####--####--####--####--##
#Exercise 13

# def f(x):
#   return x**4 - 2*x**3 - 3*x**2 + 3*x + 2

# def df(x):
#   return 4*x**3 - 6*x**2 -6*x +3

# x0 = -1.77411
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 14

# def f(x):
#   return x + 1 - 3*math.sin(x)

# def df(x):
#   return 1 - 3*math.cos(x)

# x0 = -1.56162
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 27

# def f(x):
#   return math.e**(5*x) - 2

# def df(x):
#   return 5*math.e**(5*x)

# x0 = -1.16733114
# numIteracao = 700
####--####--####--####--####--##

###--####--####--####--####--##
# PROVA - 2

#def f(x):
#  return x**2 - 2

#def df(x):
#  return 2*x

###--####--####--####

#def f(x):
#  return x**2 - 4*x + 2 - math.log(x)

#def df(x):
#  return 2*x - 4 - 1/x

#def f(x):
    
#    g = 9.81
#    c = 18.22
#    v = 39.61
#    t = 8.2

#    return ((g*x)/c) * (1 - math.e**(-(c/x)*t)) - v

#def df(x):
#    return 0.538419 * (1 - math.e**(-(149.404)/x)) - (80.442 * (math.e**(-(149.404)/x))/x)

def f(x):
  g=9.81
  v=11.07  
  t=5.72
  l=7.35
  return v - math.sqrt(2*g*x) * math.tanh(((math.sqrt(2*g*x))/(2*l))*t)

def df(x):
  return - (3* math.sqrt(109)* math.tanh((143*math.sqrt(2)*math.sqrt(109)*math.sqrt(x))/(1225)))/(5*2**(3/2)*math.sqrt(x)) - (46761 * (1/(math.cosh((143*math.sqrt(2)*math.sqrt(109)*math.sqrt(x))/(1225)))))/12250


x0= 1.0
numIteracao = 5

###--####--####--####--####--##

#   ZERO DE FUNCAO
#           Metodo de Newton
# Entrada: estimativa inicial (x0), funcao (f), derivada funcao (df), e numero de iteracoes (numIteracao)
def metodoNewton(x0,f,df,numIteracao):
  print("Calcular metodo de Newton !!\n\n")
  for i in range(numIteracao):
    if(df(x0) == 0):
      print("Divisao por zero na derivada em {}\n".format(x0))
      break
    else:
      x0 = x0 - f(x0) / df(x0)
      print("x_{} = {}\n".format(i+1,x0))

if __name__ == "__main__":
  metodoNewton(x0,f,df, numIteracao)