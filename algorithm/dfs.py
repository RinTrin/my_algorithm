# depth first search algorithm

import sys
sys.settrace
sys.setrecursionlimit(10**7) # 再起回数の設定

def dfs_recursion(now, g, mat):
    now_x, now_y = now
    # print(now)
    if now_x >= H or now_y >= W or now_x < 0 or now_y < 0:
        return None
    if mat[now_x][now_y] == '#':
        return None
    if mat[now_x][now_y] == 'g':
        print('Yes')
        exit()
    mat[now_x][now_y] = '#'   # <-- ここがポイント！！
    a=dfs_recursion([now_x+1, now_y], g, mat)
    b=dfs_recursion([now_x, now_y+1], g, mat)
    c=dfs_recursion([now_x-1, now_y], g, mat)
    d=dfs_recursion([now_x, now_y-1], g, mat)

    # if '' in set([a, b, c, d]):
    #     pass
    # else:
def dfs_stack(start, goal, mat):
    sx, sy = start
    gx, gy = goal
    h, w = np.array(mat).shape
    stack = [[sx,sy]]
    visited = [[0 for i in range(w)]for j in range(h)]
    visited[sx][sy] = 1

    dx_dy = [[1,0],[0,1],[-1,0],[0,-1]]

    while stack:
        x,y = stack.pop() #要素を取り出す
        for i in range(4):
            nx,ny = x+dx_dy[i][0], y+dx_dy[i][1] #現在の位置
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and c[nx][ny] != '#':
                visited[nx][ny] = 1 #訪れた印をつける
                stack.append([nx,ny]) #スタックに現在位置をpush
        if visited[gx][gy] == 1: 
            print("Yes")
            sys.exit()

    print("No")

import numpy as np

H, W = map(int, input().split())
c_matrix = [[i for i in input()] for _ in range(H)]
print(c_matrix)
c_plain = []
for i, cs in enumerate(c_matrix):
    for j,c in enumerate(cs):
        if c == 's':
            position_s = [i,j]
        elif c=='g':
            position_g = [i,j]
        # c_plain.append(c)

print(position_s, position_g)

dfs_recursion(position_s, position_g, c_matrix)
print('No')

# if __name__=='__main__':
#     nodes = [0]*10
#     edges = [[1, 2], [2, 3]]
#     ans = dfs(0, 10, edges)
#     print(ans)