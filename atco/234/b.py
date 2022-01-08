N = int(input())
xy_list = []
for n in range(N):
    x, y = map(int, input().split())
    xy_list.append([x, y])
ans = 0.0
import numpy as np 
for i in range(N-1):
    x1, y1 = xy_list[i]
    for j in range(i+1, N):
        x2, y2 = xy_list[j]
        dist = np.sqrt((x1-x2)**2 + (y1-y2)**2)
        if dist > ans:
            ans = dist

print(ans)