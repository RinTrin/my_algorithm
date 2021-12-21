m = int(input())
m_list = []
for _ in range(m):
    a, b = map(int, input().split())
    m_list.append([a, b])
n = int(input())
n_list = []
for _ in range(n):
    a, b = map(int, input().split())
    n_list.append([a, b])

acceptable = 0
i = 0
j = 0
m_list = sorted(m_list)
n_list = sorted(n_list)
# while True:
#     if i==m or j==n:
#         break
#     m_x, m_y = m_list[j]
#     n_x, n_y = n_list[j]
#     if m_x == n_x+distx and m_y == n_y+disty:
#         acceptable += 1
#         i+=1
#         j += 1
#         continue
#     distx, disty = m_x-n_x, m_y-n_y
#     i=0
#     j+=1

for i in range(n):
    count = 0
    distx, disty = [m_list[0][l]-n_list[i][l] for l in range(2)]
    for j in range(m):
        for k in range(n):
            if m_list[j][0]-n_list[k][0] == distx and m_list[j][1]-n_list[k][1] == disty:
                count+=1
                break
        if count == m:
            print(-distx, -disty)
            exit()
        

    

# if acceptable==m:
# print(acceptable)
# print(distx, disty)
