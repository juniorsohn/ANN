from jacobi import metodoJacobi
import math

#   SISTEMAS LINEARES
#           METODO DA ELIMINACAO DE GAUSS SEIDEL
# Entrada: matriz[lin][col], termosIndependentes[col], chute[col], numIteracao
# matriz é o sistema linear
# TI são as respostas em vetor do das equacoes do SL

def metodoGaussSeidel(matriz,ti,chute,numIteracao):
  linha=len(matriz)
  coluna=len(matriz[0])
  for it in range(numIteracao):
    for i in range(linha):
      xi = ti[i]
      for j in range(coluna):
        if i != j:
          xi -= matriz[i][j] * chute[j]
      xi /= matriz[i][i]
      chute[i] = xi
    if it == 1 or it == 6 or it == 17:
      print("X^{} -> ".format(it+1))
      for k in range(coluna):
        print("{}".format(chute[k]))
      print("")

if __name__ == "__main__":
  # A = [[9.92398, 4.56492, -3.81009], [0.50034, 2.07938, 0.03008], [2.15027, 0.9574, -4.65664]]
  # B = [-0.98735, 2.34167, 0.56992]
  # chute = [1.07522, 2.65208, 3.90839]
  # n=18

  metodoGaussSeidel(A,B,chute,n)
