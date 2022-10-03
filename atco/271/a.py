N = int(input()) 
# N, M = map(int, input().split()) 
# p_list = list(map(int, input().split())) 
# xy_matrix = [list(map(int, input().split())) for _ in range(N)] 


str_n = str(format(N, 'x'))
if len(str_n)==1:
    print('0' + str_n.upper())
else:
    print(str_n.upper())