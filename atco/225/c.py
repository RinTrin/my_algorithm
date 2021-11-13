def check_beside(b_list):
    for i in range(len(b_list)-1):
        if b_list[i+1]-b_list[i]==1:
            pass
            # print(b_list[i+1])
            # continue
        else:
            return False
    if len(b_list) == 7 and b_list[-1]%7!=0:
        return False 
    return True
def check_tate(b_start_list, b_next_list):
    for j in range(len(b_start_list)):
        if b_next_list[j]-b_start_list[j]==7:
            # print(b_next_list[j], b_start_list[j])
            # continue
            pass
        else:
            return False
    return True
def main():
    N, M = map(int, input().split())
    b_start_list = list(map(int, input().split()))
    # print('s', b_start_list)
    if N==1:
        if check_beside(b_start_list):
            return True
        else:
            return False

    for n in range(N-1):
        b_next_list = list(map(int, input().split()))
        # print('n', b_next_list)
        if check_beside(b_start_list) and check_beside(b_next_list) and check_tate(b_start_list, b_next_list):
            b_start_list = b_next_list.copy()
            # continue
        else:
            return False
    return True
    # else:
    #     return False

if __name__=='__main__':
    t = main()
    if t:
        print('Yes')
    else:
        print('No')
    # li = [1,2,3,4,5,6,7,8]
    # print(check_beside(li))
