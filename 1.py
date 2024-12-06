import numpy as np
n = int(input())
a = np.arange(n).reshape(-1,1)
for i in a:
    a[i] = int(input())
print(a.tolist())
