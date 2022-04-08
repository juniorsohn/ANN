#include<stdio.h>
#include<math.h>

void fpos(double (*f)(double), double inferior, double superior, int iteracoes){
    double fa = f(inferior);
    double fb = f(superior);

    if(fa * fb >= 0){
        printf("Impossível determinar se há raiz no intervalo [%lf,%lf]\n", inferior, superior);
        return;
    }

    double pontoMedio;
    double fx;

    for(int i = 0; i < iteracoes; i++){
        pontoMedio = ((inferior * fb) - (superior * fa)) / (fb - fa);


        printf("x_%d = %.16lf\n", i+1, pontoMedio);

        fx = f(pontoMedio);

        if(fx == 0){
            printf("A raiz é: x = %.16lf\n", pontoMedio);
            return;
        }

        if(fa * fx < 0){
            superior = pontoMedio;
            fb = fx;
        }else{
            inferior = pontoMedio;
            fa = fx;
        }

    }
}



void main(){

    double k1 = 41800;
    double k2 = 77;
    double m = 137, g = 9.81, h = 0.7;

    double f(double x){
        return (2*k2*pow(x,(5/2))/5) + (k1*(x*x)/2) - m*g*x - m*g*h;
    }

    double inferior1 = 0.00;
    double superior1 = 1.75;
    int iteracoes1 = 11;

    fpos(f, inferior1, superior1, iteracoes1);

}
