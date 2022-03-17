n, m = map(int, input().split())
c_list = list(map(int, input().split()))
dp = [[0 for _ in range(n+1)] for _2 in range(m)]
for m_, c in enumerate(c_list):
    i=1
    while c*i<=n:
        dp[m_][c*i] = i
        i+=1
    for j, val in enumerate(dp[m_-1]):
        if val > 0:
            k=0
            while val+c*k<=n:
                dp[m_][j+c*k] = min(dp[m_-1][j+c*k], val+k)
                k+=1
print(dp[-1][-1])
print(dp)
