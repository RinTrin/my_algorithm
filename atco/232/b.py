S = input()
T = input()
is_correct = True
def backword(a, b):
    a_ = ord(a)
    b_ = ord(b)
    if b_ > a_:
        abs_num = b_ - a_
    else:
        abs_num = 26 - (a_ - b_)
    return abs_num

num_before = backword(S[0], T[0])
# print(num_before)
for i in range(1, len(T)):
    num = backword(S[i],T[i])
    # print(num)
    if num_before != num:
        is_correct = False
        break

if is_correct:
    print('Yes')
else:
    print('No')