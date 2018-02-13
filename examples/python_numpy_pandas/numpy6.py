import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

C = np.vstack((A, B))  #上下合并
D = np.hstack((A, B))  #左右合并
print(A.shape, C.shape, D.shape)

print(A[:, np.newaxis])  #纵向
print(A[np.newaxis, :])  #横向

E = np.concatenate((A, B, B, A))
print(E)
