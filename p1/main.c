#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    //funçoes
    double f(double x);
    double g(double k);
    void bisection(double (*f)(double), double a, double b, int n);

    //variaveis
    double a = 0;
    double b = 2;
    int n = 15;

    //variaveis questao2
    double a2 = 0.001;
    double b2 = 2;
    int m = 50;

    //bisection(f, a, b, n);
    bisection(f, 0, 4.75, n);
    return 0;
}

double Vs(double x){
  return ((4*3.14159265359)*(pow(x, 3)))/3;
}

double V(double pw, double ps, double raio){
  return (Vs(raio)*(pw-ps))/pw;
}

double f(double x){
    return 12*(pow(x, 2)-(9.77*x)+15.6743);
}

double g(double k){
    return 1000000.0 * exp(k) + (537142.0/k) * (exp(k) - 1) - 1863961.0;
}

void bisection(double (*f)(double), double a, double b, int n){
    double fa = f(a);
    if(fa*f(b) >= 0){
        printf("Nao sei dizer se f possui raiz no intervalo [%f, %f]\n",a,b);
    }else{
        double m = 0;
        for(int i=0;i<n;i++){
            m = 0.5*(a+b);
            printf("x_%d = %.16lf\t",i+1, m);
            double fm = f(m);
            printf("f(x_%d) = %.16lf\n",i+1,fm);
            if(fm == 0){
                printf("%f eh uma raiz\n",m);
                return;
            }
            if(fa*fm < 0){
                b = m;
            }else{
                a = m;
                fa = fm;
            }
        }
    }
}