N = input() 
a,b,c = N[0], N[1], N[2]
ans = 0
ans += int(a)*100+int(b)*10+int(c)
ans += int(b)*100+int(c)*10+int(a)
ans += int(c)*100+int(a)*10+int(b)
print(ans)