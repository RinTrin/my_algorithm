N = int(input())
p_list = list(map(int, input().split()))

q_list = [0]*N
for i, p in enumerate(p_list):
    q_list[p-1] = i+1

q_str = ''
for q in q_list:
    q_str+=str(q) + ' '
print(q_str)