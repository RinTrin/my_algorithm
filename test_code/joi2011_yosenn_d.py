n = int(input())
n_list = list(map(int, input().split()))
start_num = n_list[0]
sum_num = n_list[-1]
num_list = n_list[1:-1]
dp_dict = {key:0 for key in range(20+1)}
dp_dict[start_num] += 1
for i, num in enumerate(num_list):
    next_dp_dict = {key:0 for key in range(20+1)}
    for key, val in dp_dict.items():
        if val>0:
            # dp_dict[key]=0
            value = key+num
            if 0<=value<=20:
                next_dp_dict[value]+=val
            value = key-num
            if 0<=value<=20:
                next_dp_dict[value]+=val

    dp_dict = next_dp_dict
print(dp_dict[sum_num])