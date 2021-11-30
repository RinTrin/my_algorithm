N, Q = map(int, input().split())
S = str(input())
S_list = [0]
for i in range(1, len(S)):
    if S[i-1]=='A' and S[i]=='C':
        S_list.append(S_list[i-1]+1)
    else:
        S_list.append(S_list[i-1])

for _ in range(Q):
    l, r = map(int, input().split())
    
    if S_list[l]=='C':
        l+=1
    print(S_list[r-1]-S_list[l-1])