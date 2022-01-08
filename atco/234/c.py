N = int(input())
ans = str(bin(N)[2:])

new_ans = ''
for a in ans:
    if a == '1':
        new_ans += '2'
    else:
        new_ans += '0'

# print(ans)
print(new_ans)