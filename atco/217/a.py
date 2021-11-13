S, T = map(str, input().split())
# if len(S) < len(T):
#     is_ok = True
#     for i in range(len(S)):
#         s = S[i]    
#         t = T[i]
#         if ord(s) > ord(t):
#             is_ok = False
#             break
#     if is_ok:
#         print('Yes')
#     else:
#         print('No')
# else:
#     is_ok = True
#     for i in range(len(T)):
#         s = S[i]    
#         t = T[i]
#         if ord(s) > ord(t):
#             is_ok = False
#             break
#     if S[:len(T)] == T:
#         print('No')
#     elif is_ok:
#         print('Yes')
#     else:
#         print('No')  
if S < T:print('Yes')
else:print('No')
