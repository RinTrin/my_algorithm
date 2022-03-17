n, k = map(int, input().split())
import collections
ab_dic =  collections.defaultdict(int)
for _ in range(k):
    a, b = map(int, input().split())
    ab_dic[a] = b
# mat = sorted(ab_mat, key=lambda x:x[0])
def able_three(key):
    able_list = []
    n0, n1, n2 = str(key)
    if int(n0)==int(n1) and int(n1)==int(n2):
        able_list.append(n0+n0+str(mod(int(n0)-2, 3)+1))
        able_list.append(n0+n0+str(mod(int(n0)-3, 3)+1))
    else:
        able_list.append(n1+n2+str(1))
        able_list.append(n1+n2+str(2))
        able_list.append(n1+n2+str(3))
    return able_list

def mod(value, div):
    if value%div>=0:
        return value%div
    else:
        while value%div>=0:
            value+=div
        return value%div

# three_dict = collections.defaultdict(int)
# if 1 in ab_dic.keys():
#     start =[str(ab_dic[1])]
# else:
#     start = [str(1), str(2), str(3)]
# second = []
# if 2 in ab_dic.keys():
#     for s in start:
#         second.append(s+str(ab_dic[2]))
# else:
#      for s in start:
#         second.append(s+str(1))
#         second.append(s+str(2))
#         second.append(s+str(3))
# last = []
# if 3 in ab_dic.keys():
#     for s in second:
#         last.append(s+str(ab_dic[3]))
# else:
#      for s in second:
#         last.append(s+str(1))
#         last.append(s+str(2))
#         last.append(s+str(3))
# for val in last:
#     three_dict[val] += 1
# print(three_dict)
    
# for n_ in range(4, n):
#     next_three_dict = collections.defaultdict(int)
#     if n_ in ab_dic.keys():
#         for key, val in three_dict.items():
#             next_three_dict[key[1:]+str(ab_dic[n_])]+=val
#     else:
#         for key, val in three_dict.items():
#             for able in able_three(key):
#                 next_three_dict[able] += val
#     three_dict = next_three_dict

# print(three_dict)
# print(mat)
# print(mod(2,3))
# print(mod(-1, 5))

def f(i, a, b):
    passA