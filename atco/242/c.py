N = int(input()) 
ans = 0
for i in range(1, 10):
    num_dict = [0 for i in range(1, 10)]
    ## start is i
    num_dict[i-1] +=1

    for j in range(N-1):
        new_num_dict = num_dict.copy()
        for num, nums_num in enumerate(num_dict):
            if nums_num==0:continue
            if num == 0:
                # num_dict[num]
                new_num_dict[2-1]+=(nums_num)#%998244353)
                # new_num_dict[1]+=(nums_num-1
            elif num==8:
                new_num_dict[8-1]+=(nums_num)#%998244353)
            else:
                # print(num, (nums_num)
                new_num_dict[num-1]+=(nums_num)#%998244353)
                new_num_dict[num+1]+=(nums_num)#%998244353)
        num_dict = [v for v in new_num_dict]
        # print(num_dict)
    ans+=(sum(num_dict)%998244353)
print(ans)