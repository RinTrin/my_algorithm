# N = int(input()) 
N, M, K = map(int, input().split()) 
abc_matrix = [list(map(int, input().split())) for _ in range(M)]
from collections import deque
e_list = deque(list(map(int, input().split())) )


root_value_list = []

# min_value = abc_matrix[e_list[0]][2]
# for e in e_list[1:]:
now_idx = 0
now_edge = None
while now_idx < len(e_list):
    e  =e_list.popleft()
    a, b, c = abc_matrix[e-1]
    root_value_list.append(c)
    
