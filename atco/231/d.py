

N, M = map(int, input().split())
done_list  =[]
appear_list = []
node_list = []
is_able = True
for m in range(M):
    A, B = map(int, input().split())
    if A in done_list or B in done_list:
        is_able = False
        break
    if [A, B] in node_list or [B, A] in node_list:
        is_able = False
        break
    if A not in appear_list and B not in appear_list:
        appear_list.append(A)
        appear_list.append(B)
        node_list.append([A, B])
    elif A in appear_list and B not in appear_list:
        done_list.append(A)
        appear_list.append(B)
        for x, y in node_list:
            if A == x:
                node_list.remove([x, y])
                node_list.append([B, y])
            elif A == y:
                node_list.remove([x, y])
                node_list.append([x, B])
    elif A not in appear_list and B in appear_list:
        appear_list.append(A)
        done_list.append(B)
        for x, y in node_list:
            if B == x:
                node_list.remove([x, y])
                node_list.append([A, y])
            elif B == y:
                node_list.remove([x, y])
                node_list.append([x, A])
    else:
        done_list.append(A)
        done_list.append(B)
        news = []
        for x, y in node_list:
            if x == A or x == B:
                node_list.remove([x, y])
                news.append(y)
            elif y == A or y == B:
                node_list.remove([x, y])
                news.append(x)
        node_list.append(news[0])

if is_able:
    print('Yes')
else:
    print('No')