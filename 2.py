import numpy as np

n = int(input())
m = int(input())
a = []

for i in range(n * m):
    a.append(int(input()))

a = np.array(a)
a = a.reshape(n, m)

b = []
c = []

for i in range(m):
    b.append(int(input()))

for i in range(n):
    c.append(int(input()))

b = np.array(b)

c = np.array(c)
print(a.tolist(), b.tolist(), c.tolist(), ((a + b) * (c.reshape(-1, 1)).tolist()))