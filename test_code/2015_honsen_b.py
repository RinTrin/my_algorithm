n = int(input())
a_list = []
dp_before = [0 for _ in range(n)]
for _ in range(n):
    val = int(input())
    a_list.append(val)
    left_list = [l_ for l_ in range(n) if l_ is not _]
    dp_before[_] = [val, left_list]

def div(a, n):
    if a%n>=0:
        return a%n
    else:
        return a%n + n
def mv_dp(idx,is_plus=True):
    a_max = a_list[div(idx, n)]
    left_list.pop(div(idx,n))
    if is_plue:
        dp_new[div(idx+1,n)] = value+a_list[idx+1]
        left_list.pop(div(idx+1,n))
    else:
        dp_new[div(idx-1,n)] = value+a_list[idx-1]
        left_list.pop(div(idx-1,n))
for n_ in range(n//2+1):
    dp_new = [0 for _ in range(n)]
    for i, (value, left_list) in enumerate(dp_before):
        if value==0:
            continue
        if a_list[i+1]>a_list[i-1]:
            mv_dp(i+1)
        else:
            mv_dp(i-1)
    dp_before = dp_new

print(max(dp_new))
        



