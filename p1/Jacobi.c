#include <stdio.h>
#define ROWS 3
#define COLS 3

void jacobi(double coeficientes[ROWS][COLS], double independentes[ROWS], double chute[COLS], int iteracoes){
    double aproximacao;
    double temp[COLS];
    for(int it = 0; it < iteracoes; it++){
        // isolando a n-ésima variável da n-ésima equação
        for(int i = 0; i < ROWS; i++){
            aproximacao = independentes[i];
            for(int j = 0; j < COLS; j++){
                if(i != j){ // isolando a variável na diagonal
                    aproximacao -= coeficientes[i][j]*chute[j];
                }
            }
            aproximacao /= coeficientes[i][i];
            temp[i] = aproximacao;
        }
        printf("X^(%d) -> ", it+1);
        for(int k = 0; k < COLS; k++){
            chute[k] = temp[k];
            printf("%.16lf ", chute[k]);
        }
        printf("\n");
    }
}

void main(){
  double coeficientes[ROWS][COLS] = {{-9.98599, 3.88241, -4.25169},{0.3499, -2.62142, -0.41963},{-1.24869, -1.64344, -4.74403}}; // matriz de coeficientes do sistema
  double independentes[ROWS] = {0.99034, -1.47224, -4.89481}; // matriz de termos independentes do sistema
  double chute[COLS] = {4.57049, 2.34376, -3.43089}; // chute inicial

    jacobi(coeficientes, independentes, chute, 18);
}
