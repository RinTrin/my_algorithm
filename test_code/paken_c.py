N, M = map(int, input().split())
A_matrix = [list(map(int, input().split())) for _ in range(N)]

# print(A_matrix)
sum_add_all = 0
for t1 in range(M-1):
    for t2 in range(t1+1, M):
        sum_add = 0
        for i in range(N):
            sum_add += max(A_matrix[i][t1], A_matrix[i][t2])
        if sum_add > sum_add_all:
            sum_add_all = sum_add
print(sum_add_all)