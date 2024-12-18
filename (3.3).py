a = int(input())
b = int(input())
r = [a,b]
s = [1,0]
t = [0,1]
while r[-1] != 0:
    q = r[-2] // r[-1]
    r.append(r[-2] % r[-1])
    s.append(s[-2] - q*s[-1])
    t.append(t[-2] - q * t[-1])
print(a , '*' , s[-2], '+',b,'*',t[-2],'=',r[-2])    
