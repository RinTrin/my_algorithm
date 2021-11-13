N = int(input())
# for N in range(10**8):
magic = ''
def is_bin(n):
    if n%2==0:
        return True
    else:
        return False
while True:
    if N == 0:
        break
    if is_bin(N):
        N /= 2
        magic = 'B' + magic
    else:
        N -= 1
        magic = 'A' + magic
print(magic)
if len(magic) >= 120:
    print('N', N)
    print('magic', magic)


# dp = 

