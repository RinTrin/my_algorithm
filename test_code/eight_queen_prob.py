def main():
    k = int(input())
    import itertools as its
    per = [list(p) for p in its.permutations(range(1, 9))]
    x_list = []
    y_list = []
    for _ in range(k):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    ans_p = []
    for p in per:
        is_ok = True
        for x, y in zip(x_list, y_list):
            if p[x] == y+1:
                pass
            else:
                is_ok = False
                break
        if is_ok:
            ans_p.append(p)
            break
    print(ans_p)
    ans_p_real = []
    for p in ans_p:
        for i in range(8):
            for j in range(i+1, 8):
                x_abs = abs(i+1 - p[i])
                y_abs = abs(j+1 - p[j])
                if x_abs==y_abs:
                    break
                else:
                    continue
            ans_p_real = p      
    for row in range(8):
        idx = ans_p_real[row]
        ans = '.'*(idx-1) + 'Q' + '.'*(8-idx)
        print(ans)


def test():
    for i in range(10):
        for j in range(10):
            if j == 5:
                break
        print('AFTER J')
    print('AFTER I')

if __name__=='__main__':
    test()