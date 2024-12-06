import numpy as np
from scipy.linalg import solve

A = np.array([[2, 4, 3],
[4, 9, -1],
[3, 6, 2]])
b = np.array([3, 6, 4.5])
print("A\n",A)
print("b\n",b)
x = solve(A, b)
print("x=",x)
print("A @ x - b\n",A.dot(x) - b)