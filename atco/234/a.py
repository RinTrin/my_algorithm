

def f_x(x):
    return x**2 + 2*x + 3


t = int(input())
ans = f_x(f_x(f_x(t) + t) + f_x(f_x(t)))
print(ans)