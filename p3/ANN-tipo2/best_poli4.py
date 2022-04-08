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
    #MATRIZ B
    yis = 0
    xises_yis = 0
    xises2_yis = 0
    xises3_yis = 0
    xises4_yis = 0
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
        #MatrizB
        yis += y[i]
        xises_yis +=x[i] * y[i]
        xises2_yis += y[i] * (x[i]**2)
        xises3_yis += y[i] * (x[i]**3)
        xises4_yis += y[i] * (x[i]**4)



    A = [[n,xises,xises_quadrado,xises_cubo,xises_quarta],[xises,xises_quadrado,xises_cubo,xises_quarta,xises_quinta],
        [xises_quadrado,xises_cubo,xises_quarta,xises_quinta,xises_sexta],[xises_cubo,xises_quarta,xises_quinta,xises_sexta,xises_setima],
        [xises_quarta,xises_quinta,xises_sexta,xises_setima,xises_oitava]]
    B = [yis,xises_yis,xises2_yis,xises3_yis,xises4_yis]
    a,b,c,d,e = np.linalg.solve(A,B)
    return a,b,c,d,e

x = [-4.4851, -4.1623, -4.0216, -3.8473, -3.6785, -3.4468, -3.2226, -3.1802, -3.0283, -2.7838, -2.4965, -2.3942, -2.3, -1.9553, -1.7602, -1.6765, -1.5294, -1.2864, -1.1415, -0.9189, -0.8317, -0.4843, -0.443, -0.1497, 0.047, 0.2423, 0.2769, 0.5706, 0.7442, 0.8839, 1.0498, 1.2587, 1.3612, 1.652, 1.804, 1.8965, 2.1545, 2.3884, 2.575, 2.7609, 2.9001, 2.9981, 3.1782, 3.4489, 3.6644, 3.8898, 4.0258, 4.2335, 4.2793, 4.4597, 4.7146, 4.9101]
y = [2.0092, 4.0233, 5.7226, 4.8692, 7.0893, 6.7124, 6.1837, 7.0527, 7.125, 6.8598, 7.1134, 7.9184, 6.922, 6.2622, 5.9832, 5.7256, 5.6189, 5.4166, 5.5954, 4.9568, 6.2628, 4.3296, 4.4773, 4.1755, 4.9385, 4.546, 3.9657, 4.3215, 4.8176, 4.115, 5.7367, 5.7651, 5.4215, 5.9391, 6.515, 6.4157, 6.9869, 7.5345, 7.6144, 8.1054, 8.2455, 8.751, 9.1829, 9.6172, 9.1183, 9.8022, 8.9784, 7.6658, 8.3682, 7.5496, 6.8499, 5.4094]

r = best_parabola(x,y)
print(r)
