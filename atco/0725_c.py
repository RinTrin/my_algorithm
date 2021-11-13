def gcd_more(enum_list):
    ans = gcd(enum_list[0], enum_list[1])
    for n, e in enumerate(enum_list):
        if n<2:continue
        ans = gcd(ans, e)
    return ans
def gcd(a, b):
    # a > b
    if a > b:pass
    else:
        a_past = a
        a = b
        b = a_past
    if b==0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a, b):
    return a * b / gcd(a, b)

N = int(input())
a_list = []
b_list = []
a_gcd = 0
b_gcd = 0
for n in range(N):
    a, b = map(int, input().split())
    a2a_list = a_list
    a2b_list = a_list
    b2a_list = b_list
    b2b_list = b_list
    a2a_list.append(a)
    a2b_list.append(b)
    b2a_list.append(a)
    b2b_list.append(b)
    a_gcd = max(gcd_more(a2a_list), a_gcd)
    b_gcd = (gcd_more(b_list), b_gcd)
    new_lcm1 = lcm(a_gcd, b_gcd)
    new_lcm2 = lcm(a_gcd, b_gcd)
    if lcm(a_gcd, b_gcd) > now_lcm:
        now_lcm = new_lcm
    
print(lcm(a_gcd, b_gcd))