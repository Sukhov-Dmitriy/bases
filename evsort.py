import numpy as np
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(a)
b = np.ndarray(a)
c = np.sort(a)
print(c[::-1])
