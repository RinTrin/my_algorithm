from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def main():
    def dfs(node, value):
        new_x = weight_list[node-1]
        value+=new_x
        ans_list[node-1] = value
        used_list[node-1]=1

        for new_node in node_dic[node]:
            if used_list[new_node-1]==0:
                dfs(new_node, value)
                used_list[new_node-1]=1

    n, q = map(int, input().split())
    ans_list = [0 for _ in range(n)]
    node_dic = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        node_dic[a].append(b)
        node_dic[b].append(a)

    weight_list = [0 for _ in range(n)]
    used_list   = [0 for _ in range(n)]
    for _ in range(q):
        p, x = map(int, input().split())
        weight_list[p-1] += x
    
    dfs(1, 0)
    print(" ".join(map(str, ans_list)))


if __name__=='__main__':
    main()