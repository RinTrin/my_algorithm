def main():
    N,K = map(int, input().split())
    ans_list = [[0, 0] for _ in range(N)]
    true_list = [True]*K
    ans = 1
    DIV = 998244353
    # chatty = False

    for idx in range(K):
        c, k = map(str, input().split())
        k = int(k)
        if c == 'L': 
            c_int = 1
            true_list[idx] = False
        else: c_int = 2
        ans_list[k-1] = [idx, c_int]
    print(ans_list)
    zero_time = True
    for n, id_list in enumerate(ans_list):
        print(f'{n}_true_list : {true_list}')

        if id_list[1] == 0:
            zero_time = False
            ans *= true_list.count(True)
            ans %= DIV
        elif id_list[1] == 1:
            true_list[id_list[0]] = True
        else:
            true_list[id_list[0]] = False
    print('true_list', true_list)
    if zero_time:
        print(0)
    else:
        print(ans%DIV)

if __name__ == '__main__':
    main()
    