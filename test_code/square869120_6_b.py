N = int(input())
a_list = []
b_list = []
for n in range(N):
    a, b  =map(int, input().split())
    a_list.append(a)
    b_list.append(b)

a_middle = sorted(a_list)[N//2]
b_middle = sorted(b_list)[N//2]

sum = 0
for a, b in zip(a_list, b_list):
    sum += abs(a-a_middle) + abs(b-b_middle) + abs(a-b)

print(sum)