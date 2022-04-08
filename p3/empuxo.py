import numpy as np
import math


r1 = 2.16
r2 = 5.72
H = 2.14
Pw = 1000
Pt = 553.01
pi = 'M_PI'
r3 = f'({r1}+x*({r2}-{r1})/{H})'
Hdiff = f'({H}-x)'
V = f'(({pi}*{H})/3.0)*(pow({r1},2)+pow({r2},2) + {r1}*{r2})'
Vw = f'(({pi}*{Hdiff})/3.0)*(pow({r3},2)+pow({r2},2) + {r3}*{r2})'

F = f'{Pw}*{Vw} - {Pt}*{V}'

print(F)

