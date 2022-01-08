
# for k in range(K, N+1):
#     p_use = p_list[:k]
#     p = sorted(p_use)[-K]
#     print(p)


N, K = map(int,input().split())
# p_list = list(map(lambda x: int(x)*(-1),input().split()))
p_list = list(map(int ,input().split()))
ans_list = []
ans = N-K+1
all_list = list(range(1, ans+1))

ans_list.append(ans)

for k in range(K+1, N+1):
    p_last = p_list[K-k-1]
    print('p_lst', p_last, ans, all_list)
    if ans > p_last:
        print('ans', ans)
        # ans_list.append(ans)
        all_list.remove(p_last)
    elif ans == p_last:
        # all_list.remove(ans)
        ans = all_list[-1]
        all_list.remove(ans)
        ans_list.append(ans)
    else:
        ans = all_list[-1]
        all_list.remove(ans)
        ans_list.append(ans)
        # print(all_list, ans)

# import heapq

# print(p_list)
# heapq.heapify(p_list)
# print(p_list)

# for k in range(K, N+1):
#     p_last = p_list[N-k] * (-1)
#     print(p_last)
#     if ans > p_last:
#         ans_list.append(ans)
#         trash = heapq.heappop(p_list)
#         print(ans)
#     else:
#         ans = heapq.heappop(p_list) * (-1)
#         ans_list.append(ans)
#         print('NEW', ans)
    
for a in ans_list[::-1]:
    print(a)