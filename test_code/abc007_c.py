import sys
import numpy as np
from collections import deque
sys.setrecursionlimit(10**7)
r,c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c_mat = np.array([list(str(input())) for _ in range(r)])
ans_mat = np.array([[0 for _ in range(c)] for _2 in range(r)])
# print(c_mat)
# c_mat_copy = copy.deepcopy(c_mat)
def check_4(x, y):
    four_list = [[x+1,y], [x-1,y], [x, y+1], [x, y-1]]
    able_list = []
    for f_x, f_y in four_list:
        if c_mat[f_y][f_x]==".":
            able_list.append([f_y, f_x])
    return able_list

def list_same(li, li2):
    if li[0]==li2[0] and li[1]==li2[1]:
        return True
    else:
        return False

def bfs(start_list, goal_list):
    now = start_list
    now_queue = deque()
    now_queue.append(now)
    while now_queue:
        now = now_queue.popleft()
        # print(now)
        if list_same(now, goal_list):
            # print('INTHEBREAK')
            break
        # print(check_4(now[1], now[0]))
        if check_4(now[1], now[0]) is not None:
            for y, x in check_4(now[1], now[0]):
                c_mat[y][x] = "#"
                ans_mat[y][x] = ans_mat[now[0]][now[1]] + 1
                now_queue.append([y, x])
c_mat[sy-1][sx-1] = "#"
bfs([sy-1, sx-1], [gy-1, gx-1])
# print(ans_mat)
print(ans_mat.max())

# def test():
#     print(check_4(3, 1))
# if __name__=="__main__":
#     test()
