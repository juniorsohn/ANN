#include <stdio.h>
#include <math.h>

void bisection(double (*func)(double), double inf, double sup, int iter){
    double fa = func(inf);

    if(fa * func(sup) >= 0){
        printf("Não é possível determinar raízes de f no intervalo [%lf, %lf]\n", inf, sup);
        return;
    }

    double pontoMedio = 0;

    for(int i = 0; i < iter; i++){
        pontoMedio = 0.5 * (inf + sup);
        double fm = func(pontoMedio);

        printf("x_%d = %.16lf\t", i+1, pontoMedio);
        printf("f(x_%d) = %.16lf\n", i+1, fm);

        if(fm == 0){ // caso 1, m é uma raiz
            printf("%lf é uma raíz de f\n", pontoMedio);
            return;
        }
        if(fa * fm < 0){ // caso 2, raiz está no intervalo da esquerda
            sup = pontoMedio;
        }else{ // caso 3, raiz esta no intervalo da direita
            inf = pontoMedio;
            fa = fm;
        }
    }
}

void main(){

  double f(double x){
    return 1000*((M_PI*(2.14-x))/3.0)*(pow((2.16+x*(5.72-2.16)/2.14),2)+pow(5.72,2) + (2.16+x*(5.72-2.16)/2.14)*5.72) - 553.01*((M_PI*2.14)/3.0)*(pow(2.16,2)+pow(5.72,2) + 2.16*5.72);
  }

  double inferior1 = 1.41068;
  double superior1 = 2.83991;
  int iteracoes1 = 12;


  bisection(f,inferior1, superior1, iteracoes1);

}
