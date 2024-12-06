import numpy as np

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = [x for x in a if x in b]

print(result)