N = int(input())
ans = 0

# for c in range(1, N+1):
#     for b in range(1, c+1):
#         if c*b > N:
#             break
#         for a in range(1, b+1):
#             if a*b*c <= N:
#                 ans+=1
#             else:
#                 break
# print(ans)
for n in range(1, N+1):
    div_num = make_div(n)