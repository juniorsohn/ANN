import numpy as np

def best_parabola(x,y):
    n = len(x)
    xises = 0
    #MATRIZ A
    xises = 0
    xises_quadrado = 0
    xises_cubo = 0
    xises_quarta = 0
    xises_quinta = 0
    xises_sexta = 0
    xises_setima = 0
    xises_oitava = 0
    xises_nona = 0
    xises_decima = 0
    #MATRIZ B
    yis = 0
    xises_yis = 0
    xises2_yis = 0
    xises3_yis = 0
    xises4_yis = 0
    xises5_yis = 0
    for i in range(n):
        #MatrizA
        xises += x[i]
        xises_quadrado += x[i]**2
        xises_cubo +=x[i]**3
        xises_quarta +=x[i]**4
        xises_quinta +=x[i]**5
        xises_sexta +=x[i]**6
        xises_setima +=x[i]**7
        xises_oitava +=x[i]**8
        xises_nona +=x[i]**9
        xises_decima +=x[i]**10

        #MatrizB
        yis += y[i]
        xises_yis +=x[i] * y[i]
        xises2_yis += y[i] * (x[i]**2)
        xises3_yis += y[i] * (x[i]**3)
        xises4_yis += y[i] * (x[i]**4)
        xises5_yis += y[i] * (x[i]**5)



    A = [[n,xises,xises_quadrado,xises_cubo,xises_quarta,xises_quinta],[xises,xises_quadrado,xises_cubo,xises_quarta,xises_quinta,xises_sexta],
        [xises_quadrado,xises_cubo,xises_quarta,xises_quinta,xises_sexta,xises_setima],[xises_cubo,xises_quarta,xises_quinta,xises_sexta,xises_setima,xises_oitava],
        [xises_quarta,xises_quinta,xises_sexta,xises_setima,xises_oitava,xises_nona],[xises_quinta,xises_sexta,xises_setima,xises_oitava,xises_nona,xises_decima]]
    B = [yis,xises_yis,xises2_yis,xises3_yis,xises4_yis,xises5_yis]
    a,b,c,d,e,f = np.linalg.solve(A,B)
    return a,b,c,d,e,f

x = [-4.1914, -3.8061, -3.4568, -3.4294, -3.1499, -2.8599, -2.5049, -2.227, -1.8771, -1.6024, -1.5277, -1.2053, -0.8675, -0.5376, -0.4894, -0.0994, 0.0969, 0.3396, 0.6483, 0.8724, 1.2647, 1.5251, 1.7147, 2.0064, 2.2523, 2.4745, 2.8783, 3.1353, 3.42, 3.4732, 3.9709, 4.2225]
y = [2.3092, 6.5737, 8.0664, 8.5601, 8.4573, 7.8258, 6.6017, 5.8093, 4.6126, 4.0649, 3.7812, 3.6788, 3.7643, 4.1024, 4.0441, 4.9071, 6.0908, 5.8285, 6.6683, 6.3603, 6.684, 6.2431, 5.9112, 5.1041, 4.0877, 3.3361, 2.1048, 1.8533, 1.7424, 1.7661, 2.7629, 8.0397]

r = best_parabola(x,y)
print(r)
