import numpy as np

def main():
    H, W = map(int, input().split())
    A_all = []
    for h in range(H):
        A_list = list(map(int, input().split()))
        A_all.append(A_list)

    A_all = np.array(A_all)
    print(judge_all(A_all, H, W))

def judge_each(A1, A2, A3, A4):
    sum = A2-A1 + A3-A4
    if sum>=0:
        return True
    else:
        return False


def judge_all(A_all, H, W):
    for i_1 in range(H-1):
        for i_2 in range(i_1+1, H):
            for j_1 in range(W-1):
                for j_2 in range(j_1+1, W):
                    if judge_each(A_all[i_1][j_1],A_all[i_1][j_2],A_all[i_2][j_1],A_all[i_2][j_2]):
                        pass
                    else:
                        return 'No'
    return 'Yes'

if __name__=='__main__':
    main()