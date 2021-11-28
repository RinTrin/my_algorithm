def exchange(str_list):
    new_list = []
    for letter in str_list:
        if letter == '#':
            new_list.append(1)
        else:
            new_list.append(0)
    return new_list

s1 = input()
s2 = input()
a, b = s1[0], s1[1]
c, d = s2[0], s2[1]

new_a, new_b, new_c, new_d = exchange([a, b, c, d])

ab = new_a + new_b
cd = new_c + new_d
ac = new_a + new_c
bd = new_d + new_b
is_2 = False
for lets in [ab, cd, ac, bd]:
    if lets == 2:
        print('Yes')
        is_2 = True
        break
if not is_2:
    print('No')
    