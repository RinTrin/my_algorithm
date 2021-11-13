# L, Q = map(int, input().split())
# len_data = [[0, L]]
# ans_list = []
# for q in range(Q):
#     c, x = map(int, input().split())
#     # print(f'len_data:{len_data}')
#     for data in len_data:
#         d0, d1 = data
#         if d0 < x < d1:
#             now_wood = [d0, d1]
#             break
#     # print(f'now_wood:{now_wood}')
#     if c==1:
#         len_data.pop(len_data.index(now_wood))
#         len_data.append([d0, x])
#         len_data.append([x, d1])
#     elif c==2:
#         # print('d1, d0 : ', d1, d0)
#         ans_list.append(d1-d0)
# for ans in ans_list:
#     print(ans)

L, Q = map(int, input().split())
len_data = [0, L]
ans_list = []
now_wood = 0
for q in range(Q):
    c, x = map(int, input().split())
    # print(f'len_data:{len_data}')
    for i, data in enumerate(len_data):
        if data < x < len_data[i+1]:
            now_wood = len_data[i+1]-data
            break
    # print(f'now_wood:{now_wood}')
    if c==1:
        len_data.append(x)
        len_data = sorted(len_data)
    elif c==2:
        # print('d1, d0 : ', d1, d0)
        ans_list.append(now_wood)
for ans in ans_list:
    print(ans)