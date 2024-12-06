import numpy as np

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = list(set(a)|set(b))

print(result)