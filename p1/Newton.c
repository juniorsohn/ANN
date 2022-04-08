#define _USE_MATH_DEFINES
#include<stdio.h>
#include<math.h>


void newton(double (*func)(double),double (*dfunc)(double), double chuteInicial, int iteracoes){

    for(int i = 0; i < iteracoes; i++){
        double dfx0 = dfunc(chuteInicial);

        if(dfx0 == 0){
            printf("Não é possível executar a iteração %d do método\n", i+1);
            printf("\tf'(%lf) = 0\n", chuteInicial);
            return;
        }

        chuteInicial = chuteInicial - func(chuteInicial) / dfx0;



        printf("x_%d = %.16lf\n", i+1, chuteInicial);

    }
}

void main(){


   double k1 = 41800;
    double k2 = 77;
    double m = 137, g = 9.81, h = 0.7;

    double f(double x){
         return (2*k2*pow(x,(5/2))/5) + (k1*(x*x)/2) - m*g*x - m*g*h;
    }

    double dg(double x){
        return 77*pow(x,(3/2)) + 41800*x - 1343.97;
    }

    double x0 = 3.10;

    newton(f,dg,x0,6);
}
