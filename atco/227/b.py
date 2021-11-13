N = int(input())
S_list = list(map(int, input().split()))

S_able_list = []
for a in range(1, 143):
    for b in range(1, 143):
        S_maybe = 3*a + 4*a*b + 3*b
        if S_maybe > 1000:
            continue
        S_able_list.append(S_maybe)
ans = N
for n in range(N):
    if S_list[n] in S_able_list:
        ans -= 1

print(ans)