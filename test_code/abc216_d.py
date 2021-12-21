N, M = map(int, input().split())
from collections import deque, Counter
all_ball = []
for m in range(M):
    k = int(input())
    a_list = list(map(int, input().split()))
    all_ball.append(deque(a_list))
color_able = []
c = Counter(all_ball[:][0])
for n, i in c.items():
    if i==2:
        color_able.append(n)

mask = [False]*N
while len(color_able)!=0:
    for color in color_able:
        a, b = all_ball[:][0].index(color)
        all_ball[a].popleft()
        all_ball[b].popleft()
        color_able = []
        c = Counter(all_ball[:][0])
        for n, i in c.items():
            if i==2:
                color_able.append(n)
    

if mask:
    print('Yes')
else:
    print('No')