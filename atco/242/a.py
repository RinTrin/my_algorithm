a, b, c, x = map(int, input().split()) 

if x<=a:
    print(1.0)
else:
    if a+1<=x<=b:
        print(c/(b-a))
    else:
        print(0.0)