n = int(input())
s_list = list(map(int, input().split()))
q = int(input())
t_list = sorted(list(map(int, input().split())))

# s_dic = {}
# for s in s_list:
#     s_dic[s] = 1

ans = 0
# for t in t_list:
#     # if t in s_list:
#     #     ans += 1
#     try:
#         if s_dic[t]:
#             ans += 1
#     except:
#         pass
import bisect
for t in t_list:
    pos = bisect.bisect_left(s_list, t)
    try:
        if t == s_list[pos]:
            ans += 1
    except:
        pass

print(ans)