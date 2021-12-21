import numpy as np
N = int(input())

multiple_list = []

for i in range(1, int(np.sqrt(N))+1):
    if N % i == 0:
        multiple_list.append([i, int(N/i)])
        # multiple_list.append(N/i)
# print(multiple_list)
min_len = np.inf
for mul in multiple_list:
    m1, m2 = mul
    max_len = max(len(str(m1)), len(str(m2)))
    if max_len < min_len:
        min_len = max_len

print(min_len)