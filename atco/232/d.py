def miss():
    H, W = map(int,input().split())
    mat = [[] for _ in range(H)]
    num_mat = [[0 for _ in range(W)] for _ in range(H)]
    for h in range(H):
        c_w = input()
        for c in c_w:
            mat[h].append(c)
    i = 0
    j = 0
    num_mat[0][0] = 0
    # while True:
    #     if i == H-1 and j == W-1:
    #         break
    break_is = False
    for i in range(H):
        if break_is:
            break
        for j in range(W):
            is_n = 0
            if mat[i][j] == '#':
                continue

            if i+1 == H:
                pass
            else:
                if mat[i+1][j] == '#':
                    is_n += 1
                    num_mat[i+1][j] = -100
                else:
                    num_mat[i+1][j] = max(num_mat[i][j] + 1, num_mat[i+1][j])

            if j+1 == W:
                pass
            else:
                if mat[i][j+1] == '#':
                    is_n += 1
                    num_mat[i][j+1] = -100
                else:
                    num_mat[i][j+1] = max(num_mat[i][j] + 1, num_mat[i][j+1])
            
            if is_n == 2:
                break_is = True
                break

    # print(num_mat)
    num_ans = max(max(num_mat))
    print(num_ans + 1)



"""
retry
"""

def main():
    max_n = 1
    H, W = map(int,input().split())
    mat = [[] for _ in range(H)]
    num_mat = [[0 for _ in range(W)] for _ in range(H)]
    num_mat[0][0] = 1
    for h in range(H):
        c_w = input()
        for c in c_w:
            mat[h].append(c)
    for i in range(H):
        for j in range(W):
            if mat[i][j] == '#':
                continue
            if i==0 and j==0:
                continue

            if num_mat[i-1][j] == 0 and num_mat[i][j-1]==0:
                num_mat[i][j] = 0
            else: 
                num_mat[i][j] = max(num_mat[i-1][j], num_mat[i][j-1]) + 1
                max_n = max(max_n, num_mat[i][j])
            

    # print(num_mat)
    # num_ans = max(max(num_mat))
    # print(num_ans)
    print(max_n)

if __name__ == '__main__':
    main()