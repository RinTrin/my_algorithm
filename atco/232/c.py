N, M = map(int, input().split())
dic1 = {}
dic2 = {}
for  m in range(M):
    a, b = map(int, input().split())
    dic1[a] += 1
    dic1[b] += 1
for  m in range(M):
    a, b = map(int, input().split())
    dic2[a] += 1
    dic2[b] += 1

dic1_list = list(dic1.values())
dic2_list = list(dic2.values())

start1 = dic1_list[0]
for i in range(len(dic2_list)):
    start2 = dic2_list[i]
    if start1 != start2:
        continue
    for j in range():
        pass