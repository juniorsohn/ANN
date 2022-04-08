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
    #MATRIZ B
    yis = 0
    xises_yis = 0
    xises2_yis = 0
    xises3_yis = 0
    for i in range(n):
        #MatrizA
        xises += x[i]
        xises_quadrado += x[i]**2
        xises_cubo +=x[i]**3
        xises_quarta +=x[i]**4
        xises_quinta +=x[i]**5
        xises_sexta +=x[i]**6
        #MatrizB
        yis += y[i]
        xises_yis +=x[i] * y[i]
        xises2_yis += y[i] * (x[i]**2)
        xises3_yis += y[i] * (x[i]**3)



    A = [[n,xises,xises_quadrado,xises_cubo],[xises,xises_quadrado,xises_cubo,xises_quarta],[xises_quadrado,xises_cubo,xises_quarta,xises_quinta],[xises_cubo,xises_quarta,xises_quinta,xises_sexta]]
    B = [yis,xises_yis,xises2_yis,xises3_yis]
    a,b,c,d = np.linalg.solve(A,B)
    return a,b,c,d

x = [0.2394, 0.3207, 0.6171, 0.9795, 1.2743, 1.4743, 1.8119, 1.9297, 2.182, 2.476, 2.9075, 2.9758, 3.2465, 3.7401, 3.8363, 4.2157, 4.3988, 4.6847, 4.943, 5.2626, 5.5583, 5.851, 6.1427, 6.4606, 6.5508, 6.7776, 7.2493, 7.3421, 7.6025, 7.9098, 8.1604, 8.5934, 8.7055, 9.026, 9.3033, 9.5002, 9.9973]
y = [4.717, 4.7891, 4.1116, 4.6065, 4.1541, 5.3871, 3.9654, 4.1668, 3.6707, 3.4738, 3.395, 4.3281, 4.3655, 3.2268, 4.5543, 2.9978, 2.699, 2.8136, 2.849, 3.1617, 3.1853, 2.3276, 3.3972, 3.4587, 2.5465, 2.9111, 3.787, 3.4782, 3.3982, 3.9085, 2.8899, 3.9672, 4.4578, 4.7171, 4.6653, 5.3165, 3.7177]

r = best_parabola(x,y)
print(r)
