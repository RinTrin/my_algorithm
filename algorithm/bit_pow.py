# -*- coding: utf-8 -*-
# 繰り返し二乗法による累乗和の計算->log(N)の計算量

def bit_pow(x, n):
    bin_n = bin(n)
    len_bin = len(bin_n)-2
    # print(bin_n)
    # print(len_bin)
    ans = 1
    for i in range(len_bin):
        bi = bin_n[-(i+1)]
        if int(bi)==1:
            ans *= x
        x *= x
    return ans

def bit_pow_mod(x, n, mod):
    bin_n = bin(n)
    len_bin = len(bin_n)-2
    # print(bin_n)
    # print(len_bin)
    ans = 1
    for i in range(len_bin):
        bi = bin_n[-(i+1)]
        if int(bi)==1:
            ans *= x % mod
        x *= x % mod
    return ans

if __name__ == '__main__':
    ans = bit_pow(3,7)
    print(ans)
    ans2 = bit_pow_mod(2,10,10)
    print(ans2)