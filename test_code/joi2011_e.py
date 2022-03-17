import numpy as np
h, w, n = map(int, input().split())
field_copied = np.array([list(input()) for _ in range(h)])
import copy

def search_s(field):
    for h_ in range(h):
        for w_ in range(w):
            if field[h_][w_]=="S":
                return h_, w_
def check_4(now_x, now_y):
    ok_list = []
    for add_x, add_y in [[1,0], [-1,0], [0,1], [0,-1]]:
        next_x= now_x+add_x
        next_y= now_y+add_y
        if 0<=next_x<=h-1 and 0<=next_y<=w-1:
            if field[next_x][next_y]!="X":
                ok_list.append([next_x, next_y]) 
    return ok_list
    
import collections
now_x, now_y = search_s(field_copied)

import time

st = time.time()
all_time = 0
for now_value in range(1,n+1):
    field = copy.deepcopy(field_copied)
    time_mat = np.array([[np.inf for _ in range(w)] for _ in range(h)])
    time_mat[now_x][now_y] = 0
    que = collections.deque()
    que.append([now_x, now_y])
    print(now_value, "st", time.time()-st)
    nt = time.time()
    while que:
        now_x, now_y = que.popleft()
        if field[now_x][now_y] == str(now_value):
            all_time += time_mat[now_x][now_y]
            break
        field[now_x][now_y]="X"
        for x, y in check_4(now_x, now_y):
            que.append([x, y])
            time_mat[x][y] = min(time_mat[x][y], time_mat[now_x][now_y]+1)
    print(now_value, "nt", time.time()-nt)

print(time.time()-st)
print(int(all_time))