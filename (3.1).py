def rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return rec(n-1)+rec(n-2)
n = int(input())
print(rec(n))