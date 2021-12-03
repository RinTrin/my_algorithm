n = int(input())
n_len = len(str(n))
if n >= 42:
    n_new = n+1
else:
    n_new = n
print('AGC'+'0'*(3-n_len)+str(n_new))