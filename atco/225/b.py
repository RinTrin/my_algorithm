N = int(input())
tree_side_list = []
a_0, b_0 = map(int, input().split())
a_1, b_1 = map(int, input().split())
is_finish = False
if a_0 == a_1:
    key = a_0
    tree_side_list.append(b_0)
    tree_side_list.append(b_1)
elif a_0 == b_1:
    key = a_0
    tree_side_list.append(a_1)
    tree_side_list.append(b_0)
elif b_0 == a_1:
    key = b_0
    tree_side_list.append(a_0)
    tree_side_list.append(b_1)
elif b_0 == b_1:
    key = b_0
    tree_side_list.append(a_0)
    tree_side_list.append(a_1)
else:
    is_finish = True
if is_finish:
    print('No')
else:
    is_tree = True
    for n in range(N-3):
        a, b = map(int, input().split())
        if key==a:
            tree_side_list.append(b)
        elif key==b:
            tree_side_list.append(a)
        else:
            is_tree = False
            break
    if len(set(tree_side_list)) == N-1:
        pass
    else:
        is_tree = False
    if is_tree:
        print('Yes')
    else:
        print('No')
