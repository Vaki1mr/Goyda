N = int(input())
b = int(input())
c = int(input())
N10 = 0
nst = str(N)
for i in range(len(nst)):
    N10 += int(nst[-(i+1)])* b ** i
nc = ''
while N10 > 0:
    nc += str(N10 % c)
    N10 = N10 // c
nc = nc[::-1]
print(nc)
