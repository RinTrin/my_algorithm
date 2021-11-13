xy = float(input())

import math
f, i = math.modf(xy)
f *= 10
f = int(f)
if 0<=f<=2:
    print(str(int(i))+'-')
elif 3<=f<=6:
    print(str(int(i)))
elif 7<=f<=9:
    print(str(int(i))+'+')