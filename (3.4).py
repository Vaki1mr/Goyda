f = input().split()
n = int(f[0])
s = str(f[1])
count = 1
flag = 1
count2 = 0
for i in range(n):
    print(s*count)
    if float(count) == n / 2 and count2 == 0:
        count = count
        count2 += 1
    else:
        if count >= n/2 and flag == 1:
            flag = 0
        if flag == 1:
            count += 1
        else:
            count -= 1
