N, Q = map(int, input().split()) 

li_all = []
li_length = []
for n in range(N):
    l_list = list(map(int, input().split())) 
    li_all.append(l_list[1:])
    li_length.append(l_list[0])

st_matrix = [list(map(int, input().split())) for _ in range(Q)] 


for s, t in st_matrix:
    print(li_all[s-1][t-1])