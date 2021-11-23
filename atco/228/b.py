N, X = map(int, input().split())
A_list = list(map(int, input().split()))

know_bool_list = [False for _ in range(N)]

before_know = X-1    # 0 order

for n in range(N):
    know_bool_list[before_know] = True
    next_know = A_list[before_know]-1
    before_know = next_know

know_bool_list[next_know] = True

# print(know_bool_list)
print(sum(know_bool_list))