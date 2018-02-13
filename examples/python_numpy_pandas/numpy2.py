import numpy as np

# 创建矩阵
# a = np.array([[2, 23, 4], [2, 32, 4]])
# 创建一个全部为零的矩阵
# a = np.zeros((3, 4))
# 创建一个全部为一的矩阵
# a = np.ones((3, 4), dtype=np.int64)
# 创建一个全部为空的矩阵，但实际是几乎接近为零
# a = np.empty((3, 4))
# 创建一个有序的矩阵，三个参数分别表示开始、结束、步长
# a = np.arange(10, 30, 2)
# 创建一个有序的矩阵，在基础上规定有几行几列
# a = np.arange(12).reshape((3, 4))
# 创建一个线性的矩阵，在基础上规定有几行几列
a = np.linspace(1, 10, 9).reshape((3, 3))
print(a)
