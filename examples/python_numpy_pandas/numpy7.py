import numpy as np

A = np.arange(12).reshape((3, 4))
print(A)
print(np.split(A, 2, axis=1))  # 横向分割，不能分割不对等的分割
print(np.split(A, 3, axis=0))  # 纵向分割，不能分割不对等的分割

print(np.array_split(A, 3, axis=1))  # 横向分割，能分割不对等的分割

print(np.vsplit(A, 3))  # 纵向分割
print(np.hsplit(A, 2))  # 横向分割
