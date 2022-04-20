import math

#   O método é utilizado para aproximar soluções de sistemas lineares
#   1 passo: isole uma variavel
#   SISTEMAS LINEARES
#           METODO DE JACOBI
# Entrada: matriz[lin][col], termosIndependentes[col], chute[col], numIteracao
# matriz é o sistema linear
# TI são as respostas em vetor do das equacoes do Sistema Linear
#chute são os pontos x,y,z iniciais

def metodoJacobi(matriz,ti,chute,numIteracao):
  linha=len(matriz)
  coluna=len(matriz[0])
  for it in range(numIteracao):
    tmp = []
    for i in range(linha):
      xi = float(ti[i])
      for j in range(coluna):
        if i != j:
          #xi -= matriz[j] * chute[j]  == x1 = x1 - ()
          xi = float (xi - (matriz[i][j] * chute[j]))
      #xi /= a[i] == x1 = x1/a[i]
      xi = float(xi / matriz[i][i])
      tmp.insert(i, xi)
    print("X^{} -> ".format(it+1))
    for k in range(coluna):
      print("{}".format(tmp[k]))
      chute.insert(k,tmp[k])
    print("")

if __name__ == "__main__":

  # A = [[-10.9764, -4.1375, -4.84267], [2.26031, 7.17403, -2.9175], [3.11381, -3.38176, -8.4918]]
  # B = [1.47595, 0.40306, 2.30515]
  # chute = [1.37329, -4.93343, 1.64169]
  # n=18
  A = [[1, 1.037, 1.075369, 1.115157653, 1.156418486161], [1, 1.939, 3.759721, 7.290099019, 14.135501997841],
       [1, 3.019, 9.114361, 27.516255859, 83.071576438321], [1, 5.197, 27.008809, 140.364780373, 729.475763598481],
       [1, 6.612, 43.718544, 289.067012928, 1911.311089479936]]
  B = [4.825, 4.808, 3.818, 2.215, 2.866]
  chute = [0, 0, 0, 0, 0]
  n=50

  # a     = [[6,1,-1,1],[1,-7,1,2],[2,1,9,-2],[1,2,1,-10]]
  # b     = [7,-10,-3,2]
  # chute = [0,0,0,0]
  # n     = 20

  metodoJacobi(A,B,chute,n)
