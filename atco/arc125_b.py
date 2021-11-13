# import numpy as np
# def able_sqrt(x, y):
#     func = x**2 - y
#     if func < 0:
#         return False
#     elif func==0:
#         return True
#     else:
#         # print(func)
#         func_rt = np.sqrt(func)
#         # print(func_rt)
#         return float(func_rt).is_integer()


def make_div_list(y):
    div_list = []
    # if y==1:
    #     div_list.append([1, 1])
    for i in range(1, int(y**0.5)+1):
        if y%i==0:div_list.append([int(y//i), i])
    return div_list

N = int(input())
num=0
LINE = 998244353
for y in range(1, N+1):
    for i in range(1, int(y**0.5)+1):
        if y%i==0:
            a = int(y//i)
            b = i
            if a**2 < b:
                continue
            elif (a+b)%2==0:
                num+=1
                num%=LINE
print(num)