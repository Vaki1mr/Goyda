N = int(input())
prime_dividers = []
for i in range(2,N):
    t = 0
    if N % i > 0:
        continue
    for j in prime_dividers:
        if i % j == 0:
            t = 1
    if t == 1:
        continue
    prime_dividers.append(i)
print(prime_dividers)   
x =  len(prime_dividers)
divides_pover = [0]*x
for i in range(x):
    count = 0
    while N % prime_dividers[i] == 0:
        count += 1
        N = N // prime_dividers[i]
    divides_pover[i] = count
print(divides_pover)        



