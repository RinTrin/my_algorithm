N = int(input())
S = input()
ans = 0
for i in range(1000):
    i = str(i).zfill(3)
    count = 0
    for j in range(N):
        if i[count]==S[j]:
            count+=1
        if count==3:
            ans+=1
            break
print(ans)

# -> PyPy3じゃないと通らないから注意！！



"""
pin_list = []
# pin_set = set(pin_list)
# ans = 0
for i in range(N):
    for j in range(i+1, N):
        # for k in range(j+1, N):
        for s in list(set([int(s_) for s_ in S[j+1:]])):
            # print(s)
            pin_list.append(int(S[i]+S[j]+str(s)))
        pin_set = set(pin_list)
        pin_list = list(pin_set)
print(len(pin_list))
# print(pin_list)
"""

