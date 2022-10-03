from collections import deque

N = int(input()) 
a_list = deque(list(map(int, input().split())))

now_read = 0
while True:
    # print(a_list, now_read)
    if len(a_list)==0:
        break
    a = a_list.popleft()
    if now_read+1==int(a):
        now_read += 1
    else:
        if len(a_list) >= 2:
            a_list.pop()
            a_list.pop()
            a_list.appendleft(a)
            now_read+=1
            continue
        elif len(a_list) == 1:
            a_list.pop()
            now_read += 1
            break
        else:
            break

print(now_read)