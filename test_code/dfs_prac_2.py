import copy
import sys
sys.setrecursionlimit(10**7)
m = int(input())
n = int(input())
ices = [list(map(int, input().split())) for _ in range(n)]
# ices_copy = copy.deepcopy(ices)
max_walk = 0

def search(x, y, dist):
    global max_walk
    if x<0 or y<0 or n<=x or m<=y:
        max_walk = max(max_walk, dist)
        # print(max_walk)
        return
    if ices_copy[x][y]==0:
        max_walk = max(max_walk, dist)
        # print(max_walk)
        return
    
    dist+=1
    
    ices_copy[x][y] = 0
    
    search(x+1,y, dist)
    search(x-1,y, dist)
    search(x,y+1, dist)
    search(x,y-1, dist)

for n_ in range(n):
    for m_ in range(m):
        if ices[n_][m_] == 1:
            ices_copy = copy.deepcopy(ices)
            # print('__', n_, m_)
            search(n_, m_, 0)

print(max_walk)

