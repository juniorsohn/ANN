from asyncio.tasks import _T1
import math
from telnetlib import X3PAD

def paraquedas():

#    print(f'353 + {x3} = 349 + 310')
#    print(f'{359 + 380} = {x2} + {x3}')
#    print(f'{x2} + {x1} = {1097}')
#    print(f'{490 + 527} = {353} + {x1}')
 
 
    g = 9.81
    v = 6.49

    m1 = 72.17
    c1 = 8.8

    m2 = 56.54
    c2 = 13.04

    m3 = 43.99
    c3 = 19.83

    R = 0
    T = 0

    x = m1*g - c1*v
    y = m2*g - c2*v
    z = m3*g - c3*v

    print()

    print('R' + ' - ' + str(m3) + '*a' + ' + 0T' + ' = ' + ' - ' + str(m3*g - c3*v))
    print('-' + 'R' + ' - ' + str(m2) + '*a' + ' + ' +
        'T' + ' = ' + ' - ' + str(m2*g - c2*v))
    print('0R' + ' - ' + str(m1) + '*a' + ' - ' +
        'T' + ' = ' + ' - ' + str(m1*g - c1*v))

def molas():
    import numpy as np

    g = 9.81
    m1 = 4.27
    m2 = 2.93
    m3 = 4.37
    k1 = 72.83
    k2 = 52.3
    k3 = 90.84

    K = [
        [k1+k2,     -k2,        0],
        [-k2,        (k2+k3),   -k3],
        [0,        -k3,   k3]
    ]
    X = []
    W = [m1*g, m2*g, m3*g]

    MATRIZ_K = np.array(K)
    MATRIZ_W = np.array(W)
    MATRIZ_K_INVERSA = np.linalg.inv(MATRIZ_K)

    print('K =\n', MATRIZ_K)
    print('\nK^-1 * W =', np.dot(MATRIZ_K_INVERSA, MATRIZ_W), '\n')


def blocoinclinado():
    import numpy as np
    from math import cos, sin, pi

    g = 9.81
    m1 = 198
    m2 = 59
    m3 = 44
    u1 = 0.2
    u2 = 0.26
    u3 = 0.32
    angulo = 33*pi/180

    f1 = u1*m1*g*cos(angulo)
    f1h = m1*g*sin(angulo)
    bloco1 = f'-T {f1h} -({f1}) = {m1}*a'

    f2 = u2*m2*g*cos(angulo)
    f2h = m2*g*sin(angulo)
    bloco2 = f'+T -R {f2h} -({f2}) = {m2}*a'

    f3 = u3*m3*g*cos(angulo)
    f3h = m3*g*sin(angulo)
    bloco3 = f'+R {f3h} -({f3}) = {m3}*a'


    print('bloco1 =', bloco1)
    print('bloco2 =', bloco2)
    print('bloco3 =', bloco3)

def trianguloengracado(): #treliça "easy"
    import numpy as np
    np.set_printoptions(suppress=True)
    from math import cos, sin, pi

    alpha = 57*pi/180
    beta = 52*pi/180
    F = 2895


    f1 = 0
    f2 = 0
    f3 = 0
    h2 = 0
    v2 = 0
    v3 = 0
    f1h = '0, 0, 0'
    f1v = '0, 0, 0'
    f2h = '-1, 0, 0'
    f2v = '0, -1, 0'
    f3h = '0, 0, 0'
    f3v = '0, 0, -1'

    no1Fh = f'[{cos(alpha)}, {0}, {-cos(beta)}, {f1h}]'
    no1Fv = f'[{sin(alpha)}, {0}, {sin(beta)},  {f1v}]'

    no2Fh = f'[{-cos(alpha)}, {-1}, {0},  {f2h}]'
    no2Fv = f'[{-sin(alpha)}, {0}, {0},  {f2v}]'

    no3Fh = f'[{0}, {1}, {cos(beta)}, {f3h}]'
    no3Fv = f'[{0}, {0}, {-sin(beta)}, {f3v}]'


    m = [eval(no1Fh), eval(no1Fv), eval(no2Fh),
        eval(no2Fv), eval(no3Fh), eval(no3Fv)]

    A = np.array(m)
    print('matriz =')
    print(A)

    print('inversa =')
    print(np.linalg.inv(A))

    X = [f1, f2, f3, h2, v2, v3]
    B = [0, -F, 0, 0, 0, 0]
    F_t = [f1h, f1v, f2h, f2v, f3h, f3v]

    print('resposta = ', np.linalg.solve(A, B))



if __name__ == "__main__":
    #paraquedas()
    #molas()
    #blocoinclinado()
    trianguloengracado()
