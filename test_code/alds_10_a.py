n = int(input())

li = [0 for _ in range(n+1)]
li[0] = 1
li[1] = 1
for n_ in range(2, n+1):
    li[n_] = li[n_-1]+li[n_-2]
print(li[n])