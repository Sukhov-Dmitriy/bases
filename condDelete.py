import numpy as np
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = np.array(a)
indices_to_delete = np.where(((a > 13) | (a <= 6)) & ((a%7 == 3) | (a%7 == 5)))[0]
print(indices_to_delete)
a = np.delete(a, indices_to_delete)

print(a.tolist())