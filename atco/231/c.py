N, Q = map(int,input().split())
A_list = list(map(int, input().split()))
A_sorted = sorted(A_list)
import bisect
for q in range(Q):
    x = int(input())
    key_last = bisect.bisect_left(A_sorted, x)
    print(N - key_last)
# x_list = []
    # print(key_last)
    # print('')
    # if key_last in A_list:
    #     print(N - key_last)
    # else:
    # x_list.append(x)
