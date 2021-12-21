def main():
    N,K = map(int, input().split())
    ans_list = [[0, 0] for _ in range(N)]
    true_list = [True]*K
    ans = 1
    DIV = 998244353

    for idx in range(K):
        c, k = map(str, input().split())
        k = int(k)
        if c == 'L': 
            c_int = 1
            true_list[idx] = False
        else: c_int = 2
        ans_list[k-1] = [idx, c_int]
    for idx, c in ans_list:
        if c == 0:
            ans *= true_list.count(True)
            ans %= DIV
        elif c == 1:
            true_list[idx] = True
        else:
            true_list[idx] = False
    print(ans%DIV)

if __name__ == '__main__':
    main()
    