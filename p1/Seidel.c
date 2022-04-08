#include <stdio.h>
#define ROWS 4
#define COLS 4

void seidel(double coeficientes[ROWS][COLS], double independentes[ROWS], double chute[COLS], int iteracoes){
    double aproximacao;
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
            chute[i] = aproximacao;
        }
        printf("X^(%d) -> ", it+1);
        for(int k = 0; k < COLS; k++){
            printf("%.16lf ", chute[k]);
        }
        printf("\n");
    }
}

void main(){
    double coeficientes[ROWS][COLS] = {{-10.27311, 4.28978, 0.15926, 3.8859},{2.55667, -9.36428, 4.86326, 0.00618},{2.78893, 4.01403, -10.73165, 1.99052},{-4.76325, 1.94535, -3.34871, 11.99548}}; // matriz de coeficientes do sistema
    double independentes[ROWS] = {-2.15177, 0.67625, -3.10491, -3.96974}; // matriz de termos independentes do sistema
    double chute[COLS] = {0.08352, -1.61869, -0.40565, 0.69594}; // chute inicial

    seidel(coeficientes, independentes, chute, 18);
}
