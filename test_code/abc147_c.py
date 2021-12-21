N = int(input())
dic = {}
for n in range(N):
    A = int(input())
    xy_list = [list(map(int,input().split())) for a in range(A)]
    dic[n] = xy_list
sum_max = 0

for n in range(2**N):
    is_break = False
    is_ok = False
    for i in range(1, N+1):
        if n >> i & 1:
            xy_list = dic[i]
            for x, y in xy_list:
                if not n >> x ^ y:
                    is_ok = True
                    pass
                else:
                    is_ok = False
                    is_break = True
                    break
        if is_break:
            break
    if is_break:
        continue
    if is_ok:
        sum = 0
        for bin_n in bin(n)[2:]:
            sum += int(bin_n)
            if sum_max < sum:
                sum_max = sum
        
print(sum_max)
