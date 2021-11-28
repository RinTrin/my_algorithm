# def my_max(a,b,c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# N, W = map(int, input().split())
# # old_list = [0 for _ in range(W+1)]
# # new_list = [0 for _ in range(W+1)]
# new_list = [[0, 0]]
# for n in range(N):
#     A, B = map(int, input().split())
#     for i, a in enumerate(new_list):
#         for b in range(1, B+1):
#             if i==0:
#                 new_list[i+b] = max(a + A*b, new_list[i+b])
#             elif a==0 or i+b > W:
#                 continue
#             else:
#                 new_list[i+b] = max(a + A*b, new_list[i+b])
    # print(old_list, new_list)
    # old_list = new_list.copy()
N, W = map(int, input().split())
# old_list = [0 for _ in range(W+1)]
# new_list = [0 for _ in range(W+1)]
new_list = [0]
idx_list = [0]
for n in range(N):
    A, B = map(int, input().split())
    for idx, data in zip(idx_list, new_list):
        for b in range(1, B+1):
            if idx+b > W:
                continue
            else:
                if idx+b in idx_list:
                    new_list[idx+b] = max(data + A*b, new_list[idx+b][1])
                else:
                    idx_list.append(idx+b)
                    new_list.append(data + A*b)
               
print(new_list[-1][1])
# idx = 0
# while True:
#     idx += 1
#     if new_list[-idx] != 0:
#         print(new_list[-idx])
#         break

