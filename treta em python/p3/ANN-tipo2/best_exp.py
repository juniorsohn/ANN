import math
import random
import numpy as np
from typing import List

#x = a + (b-a) * np.random.rand(10)
#x.sort()
x = [0.0534, 0.098, 0.1582, 0.2141, 0.2831, 0.3618, 0.4076, 0.4837, 0.5138, 0.589, 0.6726, 0.7178, 0.7549, 0.8682, 0.9203, 0.963, 1.0531, 1.0988, 1.1637, 1.2403, 1.2547, 1.3571, 1.4003, 1.4894, 1.5534, 1.5661, 1.6795, 1.701, 1.7832, 1.871, 1.8852, 1.9388, 2.0299, 2.1128, 2.1697, 2.2442, 2.2747, 2.3533, 2.3876, 2.4388, 2.5298, 2.5718, 2.647, 2.7165, 2.7882, 2.8204, 2.9289, 2.9446]
y = [2.4227, 3.0719, 2.6194, 2.8713, 3.6781, 2.7974, 2.8346, 3.9455, 3.0825, 3.5198, 3.6489, 3.6467, 3.325, 3.744, 3.3361, 4.0529, 3.6823, 4.0685, 4.157, 3.5681, 4.3206, 4.7726, 4.9711, 4.7487, 5.3721, 5.1996, 5.3388, 6.4554, 5.571, 7.9148, 4.7073, 5.8918, 5.8145, 6.4462, 6.9171, 7.8475, 7.3849, 7.5156, 7.7507, 7.8639, 8.0359, 8.0071, 10.2005, 8.8436, 8.8086, 9.399, 9.6539, 9.661]
def best_exp(x: List[float],y: List[float]):
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    A = [[len(x),sum_x],[sum_x,sum_x2]]
    y_ = [math.log(yi) for yi in y]
    sum_xy = sum(xi * yi for xi,yi in zip(x,y_))
    B = [sum(y_),sum_xy]
    a0,a1 = np.linalg.solve(A,B)
    a,b = math.exp(a0),a1
    return a,b

r = best_exp(x,y)
print(r)