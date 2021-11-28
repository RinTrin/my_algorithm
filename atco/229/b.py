A, B = map(int, input().split())
A_str = str(A)
B_str = str(B)
if len(A_str) >= len(B_str):
    long_len = len(A_str)
    short_len = len(B_str)
else:
    long_len = len(B_str)
    short_len = len(A_str)

is_hard = False
for i in range(short_len):
    a = A_str[-(i+1)]
    b = B_str[-(i+1)]
    if int(a) + int(b) >= 10:
        print('Hard')
        is_hard = True
        break
if is_hard:
    pass
else:
    print('Easy')