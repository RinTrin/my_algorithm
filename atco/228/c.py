import numpy as np
N, K = map(int, input().split())
p_list_all = []
for n in range(N):
    p1, p2, p3 = map(int, input().split())
    p_list_sum = p1 + p2 + p3
    p_list_all.append(p_list_sum)

# p_sorted = np.argsort(p_list_all, axis=0)
for n in range(N):
    p_list_all[n] += 300

    p_sort = np.argsort(p_list_all, axis=0)

    p_list_all[n] -= 300
    if N-int(np.where(p_sort == n)[0])-1 <= K-1:
        print('Yes')
    else:
        print('No')