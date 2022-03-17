"""
h,w = map(int, input().split())
import numpy as np
mat = np.array([list(input()) for _ in range(h)])
mat_sum_sharp = np.sum(mat=="#")

import collections
que = collections.deque()
walk_mat = [[np.inf for _ in range(w)] for _ in range(h)]
walk_mat[0][0] = 0
que.append([0,0])
mat[0][0]  ="#"
def check_4(x,y):
    li = []
    for nx, ny in [x+1, y],[x-1,y],[x,y+1],[x,y-1]:
        if 0<=nx<=h-1 and 0<=ny<=w-1:
            if mat[nx][ny]!="#":
                li.append([nx, ny])
    return li

while que:
    x, y = que.popleft()
    mat[x][y]="#"
    for next_x, next_y in check_4(x, y):
        que.append([next_x, next_y])
        walk_mat[next_x][next_y] = min(walk_mat[next_x][next_y], walk_mat[x][y]+1)

# print(walk_mat[h-1][w-1])
# print(mat_sum_sharp)
if walk_mat[x][y]==0:
    print(-1)
else:
    print(h*w-walk_mat[h-1][w-1]-mat_sum_sharp-1)

"""

#####################################################################
##############            NO NUMPY FOR PYPY3            #############
#####################################################################


h,w = map(int, input().split())
mat = [input() for _ in range(h)]
mat_sum_sharp=0
for h_ in range(h):
    for w_ in range(w):
        if mat[h_][w_]=="#":
            mat_sum_sharp+=1

from collections import deque
que = deque()
que.append([0,0,0])
mat_copy = [[0 for _ in range(w)] for _ in range(h)]
mat_copy[0][0]=1
import sys

while que:
    count, x, y = que.popleft()
    # mat_copy[nx][ny]=1 ### ここはng    -------->>>>>なんで？？？？
    if x==h-1 and y==w-1:
        print(int(h*w-count-mat_sum_sharp-1))
        sys.exit()
    for nx, ny in [x+1, y],[x-1,y],[x,y+1],[x,y-1]:
        if 0<=nx<=h-1 and 0<=ny<=w-1:
            if mat[nx][ny]!="#" and mat_copy[nx][ny]!=1:
                mat_copy[nx][ny]=1 ### ここはok
                que.append([count+1, nx, ny])
print(-1)
