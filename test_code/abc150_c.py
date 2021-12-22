N = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

import itertools as its

sorted_n = sorted(list(its.permutations(range(1, N+1))))
# print(sorted_n)

a = sorted_n.index(tuple(p_list))
b = sorted_n.index(tuple(q_list))

print(abs(a-b))