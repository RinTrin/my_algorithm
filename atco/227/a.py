N, K, A = map(int, input().split())

ans = ((A+K-1)%N)
if ans != 0:
    print(ans)
else:
    print(N)
