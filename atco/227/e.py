
# from typing import Type
import math

def change_spell(key_str, num, str_list, str_all_len):
    if num == 0 or len(str_list) == str_all_len:
        return str_list
    len_str = len(key_str)
    for i in range(len_str-1):
        before = key_str[i]
        after  = key_str[i+1]
        key_str = key_str[:i] + after + before + key_str[i+2:]
        if key_str in str_list:
            pass
        else:
            str_list.append(key_str)
        str_list = change_spell(key_str, num-1, str_list, str_all_len)
    return str_list


S = str(input())
K = int(input())
import itertools

S_len = len(S)

key_dic = {'K':0, 'E':0, 'Y':0}
for s in S:
    key_dic[s]+=1
for key, value in key_dic.items():
    if value==0:
        key_dic[key] = 1

# all = itertools.product(S, repeat=S_len)
all_len = int(math.factorial(S_len) / (math.factorial(key_dic['K'])*math.factorial(key_dic['E'])*math.factorial(key_dic['Y'])))
# all_len = len(list(all))
print(all_len)

S_list = []
# S_set_len = len(set(S_list))

S_list = change_spell(S, K, S_list, all_len)
print(len(S_list))