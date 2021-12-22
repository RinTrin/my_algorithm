# import heapq

# a = heapq.heappush(a_list)
# b = heapq.heappush(b_list)
# c = heapq.heappush(c_list)
# ans = 0
# while True:
#     if a<b<c:
#         ans += 1
#     elif a<b and not b<c:
#         c = heapq.heappush(c_list)
#     elif not a<b and b<c:
#         b = heapq.heappush(b_list)
#     else:
#         c = heapq.heappush(c_list)

N = int(input())
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())))
c_list = sorted(list(map(int, input().split())))
# print(a_list)
# print(b_list)
# print(c_list)
import bisect
ans = 0
for a in a_list:
    b_place = bisect.bisect_left(b_list, a)
    # try:
    if len(b_list[b_place:])==0:
        pass
    elif a == b_list[b_place]:
        b_place+=1
    # except:
    #     print(b_list)
    #     print(b_place)
    #     print(a)
    #     raise ValueError
    # print(b_list[b_place:])
    # print('b', b_place)
    for b in b_list[b_place:]:
        c_place = bisect.bisect_left(c_list, b)
        if len(c_list[c_place:])==0:
            pass
        elif b==c_list[c_place]:
            c_place+=1
        # print('c', c_place)
        ans += N - c_place
print(ans)