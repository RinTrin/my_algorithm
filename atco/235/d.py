a, N = map(int, input().split()) 
import sys
sys.setrecursionlimit(100000) 
times = 0
ans_list = []
def make_one(subject, times):
    global ans_list
    print(subject, times)
    if subject==1:
        return times
    if subject%a==0:
        x =  make_one(subject//a, times+1)
        if x is not None:
            ans_list.append(x)
    if int(str(subject)[-1])==0 or len(str(subject))==1:
        pass        
    else:
        new_subject = int(str(subject)[-1] + str(subject)[1:-1] + str(subject)[0])
        if new_subject%a==0:
            y =  make_one(new_subject//a, times+2)
            if y is not None:
                ans_list.append(y)
        
make_one(N, times)
if len(ans_list)> 0:
    print(ans_list[0])
else:
    print(-1)
