from collections import defaultdict

ans = ""
def main():
    def dfs(node, value):
        new_x = weight_list[node-1]
        value+=new_x
        global ans
        ans += str(value) + " "

        for new_node in node_dic[node]:
            dfs(new_node, value)

    n, q = map(int, input().split())
    node_dic = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        node_dic[a].append(b)

    weight_list = [0 for _ in range(n)]
    for _ in range(q):
        p, x = map(int, input().split())
        weight_list[p-1] += x
    
    dfs(1, 0)
    print(ans)


if __name__=='__main__':
    main()