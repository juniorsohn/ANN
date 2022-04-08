#include <stdio.h>
#include <math.h>

void main(){

    double f1 (double x, double y){
        return 4 * x * x - y * y - 5;
    }

    double f2 (double x, double y){
        return x * x + y * y * y - 4;
    }

    double det (double x, double y){
        // aparentemente essa porra tem que ficar com o sinal invertido
        return 24 * x * y * y - 4 * x * y;
    }

    double eq1(double x, double y){
        return x + (1 / det(x,y)) * ((3 * y * y) * f1(x,y) - (2 * y) * f2(x,y));
    }

    double eq2(double x, double y){
        return y + (1 / det(x,y)) * ((- 2 * x) * f1(x,y) + (8 * x) * f2(x,y));
    }

    double x0 = 1.336;
    double y0 = 1.5184;
    int iteracoes = 4;

    double x1;
    double y1;
    for(int i = 0; i < iteracoes; i ++){
        x1 = eq1(x0, y0);
        y1 = eq2(x0, y0);

        printf("x_%d = %.16lf \ty_%d = %.16lf \n", i+1, x1, i+1, y1);

        x0 = x1;
        y0 = y1;
    }

}
