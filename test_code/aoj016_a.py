N, K = map(int, input().split())
a_list = list(map(int, input().split()))

S0 = 0
S_list = []
for k in range(K):
    S0+=a_list[k]
S_list.append(S0)
for i in range(K, len(a_list)):
    S_list.append(S_list[i-K]+a_list[i]-a_list[i-K])
print(max(S_list))