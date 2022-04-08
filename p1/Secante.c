#include<stdio.h>
#include<math.h>

void secant(double (*f)(double), double inf, double sup, int iteracoes){
    double x2, fx0, fx1;

    for(int i = 0; i < iteracoes; i++){
        fx0 = f(inf);
        fx1 = f(sup);

        if((fx1 - fx0) == 0){
            printf("Divisão por 0 na iteração %d\n", i+1);
            return;
        }

        x2 = (inf * fx1 - sup * fx0)/ (fx1 - fx0);

        printf("x_%d = %.16lf\n", i+2, x2);

        inf = sup;
        sup = x2;
    }

}

void main(){

    double k1 = 41800;
    double k2 = 77;
    double m = 137, g = 9.81, h = 0.7;

    double f(double x){
        return 1000*((M_PI*(2.14-x))/3.0)*(pow((2.16+x*(5.72-2.16)/2.14),2)+pow(5.72,2) + (2.16+x*(5.72-2.16)/2.14)*5.72) - 553.01*((M_PI*2.14)/3.0)*(pow(2.16,2)+pow(5.72,2) + 2.16*5.72);
    }

    double x0 = 1.06;
    double x1 = 2.03;

    secant(f, x0, x1, 8);

    /*double g(double x){
        return pow(x,10) - 1;
    }
    */

    // double x0 = 2;

}
