N = int(input()) 
h_list = list(map(int, input().split())) 

h_now = h_list[0]
for n in range(1, N):
    h_next = h_list[n]
    if h_next > h_now:
        h_now = h_next
    else:
        break
print(h_now)
