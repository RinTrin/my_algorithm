N, K = map(int, input().split())
A_list = list(map(int, input().split()))
from itertools import permutations
pers = permutations([i for i in range(1, N+1)], N)
per_list = [list(per) for per in pers]
sort_list = sorted(per_list)
for per in sort_list:#[::-1]:
    is_ans = True
    print(per)
    for i in range(K-1):
        print('i', i)
        if per.index(A_list[i]) > per.index(A_list[i+1]):
            is_ans = False
            break
    if is_ans:
        ans = per
        break
print(ans)