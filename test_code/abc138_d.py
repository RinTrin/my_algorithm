# N, Q = map(int, input().split())

# node_dic = {n:[] for n in range(1, N+1)}
# point_dic = {n:0 for n in range(1, N+1)}
# for n in range(N-1):
#     a, b = map(int, input().split())
#     node_dic[a].append(b)
#     # node_dic[b].append(a)

# from collections import deque
# p_dic = {}
# for q in range(Q):
#     p, x = map(int, input().split())
#     if p in p_dic.keys():
#         p_dic[p] += x
#     else:
#         p_dic[p] = x

# next_node_queue = deque()
# print(p_dic)
"""
for p, xs in p_dic.items():
    # point_dic[p] += xs
    next_node_queue.append(p)
    # print(len(next_node_queue))
    while True:
        if len(next_node_queue) == 0:
            break
        next_node = next_node_queue.pop()
        # print(next_node)
        # print(next_node_queue)
        point_dic[next_node] += xs
        for node in node_dic[next_node]:
            next_node_queue.append(node)
"""

N, Q = map(int, input().split())

node_dic = {n:[] for n in range(1, N+1)}
point_dic = {n:0 for n in range(1, N+1)}
for n in range(N-1):
    a, b = map(int, input().split())
    node_dic[a].append(b)

from collections import deque
for q in range(Q):
    p, x = map(int, input().split())
    point_dic[p] += x

next_node_queue = deque()
next_node_queue.append(1)
before_node = -1
while True:
    if len(next_node_queue) == 0:
        break
    next_node = next_node_queue.popleft()
    if before_node == -1:
        pass
    else:
        point_dic[next_node] += point_dic[before_node]
    before_node = next_node
    for node in node_dic[next_node]:
        next_node_queue.append(node)

ans = ' '
ans = ans.join([str(point) for point in point_dic.values()])
print(ans)