S_list = []
S_all = ['ABC', 'ARC', 'AGC', 'AHC']
for i in range(3):
    S = str(input())
    S_list.append(S)

for s in S_all:
    if s in S_list:
        continue
    else:
        print(s)