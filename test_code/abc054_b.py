P = float(input())

import math
ps = P*math.log(2)
x = (3/2) * math.log2((2/3)*ps)
f = x + (3/2)*(1/math.log(2))
if x < 0:
    print(P)
else:
    print(f)