sp = list(map(int , input().split()))
maxx = 0
num = 0
for i in range (len(sp)) :
    if sp.count(sp[i]) > maxx:
        maxx = sp.count(sp[i])
        num = sp[i]
print(num)