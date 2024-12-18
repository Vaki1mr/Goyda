list_a = input().split()
for i in range(0, len(list_a) // 2 , 2):list_a[i] , list_a[i+1] = list_a[i+1],list_a[i]
print(list_a)