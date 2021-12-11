N = int(input())
S_list = {}
for n in range(1, N+1):
    S = input()
    if S in S_list.keys():
        S_list[S] += 1
    else:
        S_list[S] = 1
# print(S_list)

v_max = 0
ans = None
for key, value in S_list.items():
    if value > v_max:
        v_max = value
        ans = key
print(ans)