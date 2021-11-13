S = str(input())
a,b,c = S[0], S[1], S[2]
set_num = len(set([a,b,c]))
if set_num==3:print(6)
elif set_num==2:print(3)
elif set_num==1:print(1)