import math

#   ZERO DE FUNCAO
#           METODO DO PONTO FIXO
# Entrada: aproximacao inicial (x), funcao (f), erro (err) e numero de iteracoes (numIteracao)

def metodoPontoFixo(x, f, err, numIteracao):
  for i in range(numIteracao):
    x1 = f(x)
    print("x_{} = {}\n".format(i+1,x1))
    if x1 < err:
      break
    x = x1


if __name__ == "__main__":
  a=0
