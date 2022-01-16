from collections import defaultdict

N, Q = map(int, input().split()) 
a_list = list(map(int, input().split())) 
a_dic  = defaultdict(list)
for i, a in enumerate(a_list):
    a_dic[a].append(i+1)
for q in range(Q):
    x, k = map(int, input().split()) 
    try:
        print(a_dic[x][k-1])
    except:
        print(-1)
    # if (not x in a_dic.keys()) or (len(a_dic[x]) < k):
    #     print(-1)
    # else:
        # print(a_dic[x][0])
        # print(x, k-1)
# xk_matrix = [list(map(int, input().split())) for _ in range(Q)] 
