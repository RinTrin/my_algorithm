w, h = map(int, input().split())
wor_map = [list(map(int, input().split())) for _ in range(h)]

island_num = 0

def dfs(x, y, is_continue=False):
    if is_continue:
        island_num+=1
        is_continue = False
    if wor_map[x][y] == 0 or x<0 or y<0 or w<=x or h<=y:
        return
    
    
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(0,0)
print(island_num)