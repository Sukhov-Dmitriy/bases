import numpy as np
from scipy.linalg import eig

A = np.array([[1, 2],
[2, 1]])
print("A\n",A)

val, vect = eig(A)

print("val, vect = eig(A) val=",val)
print("val, vect = eig(A) vect=\n",vect)
print("vect[:,0]\n",vect[:,0])
print("A @ vect[:, 0] - val[0] * vect[:, 0]\n",A @ vect[:, 0] - val[0] * vect[:, 0])