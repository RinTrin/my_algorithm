abcd = input()
a, b, c, d = abcd[0], abcd[1], abcd[2], abcd[3]

for i in range(8):
    # i_bin = bin(i)
    sum = int(a)
    sum_string = a
    for j in range(3):
        if i >> j & 1:
            sum += int(abcd[j+1])
            sum_string += '+'+abcd[j+1]
        else:
            sum -= int(abcd[j+1])
            sum_string += '-'+abcd[j+1]
    if sum == 7:
        print(sum_string+'=7')
        break
