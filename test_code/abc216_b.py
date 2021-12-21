N = int(input())
ST_list = []
for n in range(N):
    S, T = map(str, input().split())
    ST_list.append(S + ' ' + T)
if len(ST_list) != len(list(set(ST_list))):
    print('Yes')
else:
    print('No')
        
