
N, S = map(int, input().split()) 
# p_list = list(map(int, input().split())) 
ab_matrix = [list(map(int, input().split())) for _ in range(N)] 

a_1, b_1 = ab_matrix[0]

dp_ht_dict = {}
dp_ht_dict[a_1-1] = "H"
dp_ht_dict[b_1-1] = "T"
for a, b in ab_matrix[1:]:
    dp_ht_dict_new = {}
    for key, value in dp_ht_dict.items():
        if key+a<S:
            dp_ht_dict_new[key+a]=dp_ht_dict[key]+"H"
        if key+b<S:
            dp_ht_dict_new[key+b]=dp_ht_dict[key]+"T"
    dp_ht_dict = dp_ht_dict_new


if S-1 in dp_ht_dict.keys():
    print("Yes")
    print(dp_ht_dict[S-1])
else:
    print("No")

    
"""
dp_index_list = []
dp_ht = []
a_1, b_1 = ab_matrix[0]
dp_index_list.append(a_1-1)
dp_index_list.append(b_1-1)
dp_ht.append("H")
dp_ht[b_1-1] = "T"

for a, b in ab_matrix[1:]:
    dp_index_list_new = []
    dp_ht_new = ["" for _ in range(S)]
    for idx in dp_index_list:
        is_over1, is_over2 = False, False
        if idx+a >= S:
            dp_ht_new[idx] = dp_ht[idx]
            is_over1=True
        else:
            dp_ht_new[idx+a] = dp_ht[idx] + "H"
            dp_index_list_new.append(idx+a)

        if idx+b >= S:
            dp_ht_new[idx] = dp_ht[idx]
            is_over2=True
        else:
            dp_ht_new[idx+b] = dp_ht[idx] + "T"
            if idx+a==idx+b:
                pass
            else:
                dp_index_list_new.append(idx+b)
        if is_over1 or is_over2:
            dp_index_list_new.append(idx)

            
        # print(idx, dp_index_list, idx+a, idx+b)
        # print(dp_ht_new)
    dp_index_list = dp_index_list_new
    dp_ht = dp_ht_new
"""
    