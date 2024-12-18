import numpy as np
n = 2
m = 10
N = np.zeros((n,m))
count = 1
dx = 1
dy = 0
x = 0
y = 0
for i in range(n*m):
    N[y][x] = count 
    count = count +  1
    if (x + dx < m) and (y + dy < n) and (x + dx >-1) and (y+dy > -1) and N[y+dy][x+dx] == 0:
        
        x = x + dx 
        y = y + dy
    else:
        dx, dy = -dy, dx
        x = x + dx 
        y = y + dy

print(N) 
print(np.rot90(N,k=-1))
   