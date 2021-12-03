N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

b = B-A 
c = A+B

for x in range(P, Q+1):
    ans = ''
    for y in range(R, S+1):
        if y == x + b or y == -x + c:
            ans += '#'
        else:
            ans += '.'
    print(ans)

        # if x in [x_max1, x_min1] and y in [y_max1, y_min1]:
        #     ans += '#'
        # elif x in [x_max2, x_min2] and y in [y_max2, y_min2]:
        #     ans += '#'
# for k in range():
#     raw_drawed = ''
# # first
# x_max1 = max(1-A, 1-B) + A-P
# x_min1 = min(N-A, N-B) + A-P
# y_max1 = max(1-A, 1-B) + B-R
# y_min1 = min(N-A, N-B) + B-R
# # second
# x_max2 = max(1-A, B-N) + A-P
# x_min2 = min(N-A, B-1) + A-P
# y_max2 = max(1-A, B-N) + B-R
# y_min2 = min(N-A, B-1) + B-R