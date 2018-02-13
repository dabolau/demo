import numpy as np

# 创建一个数组
# a = np.array([10, 20, 30, 40])
# 创建一个从0-3的数组
# b = np.arange(4)
# c = a - b
# print(a)
# print(b)
# print(c)

# 创建a和b两个矩阵
# a = np.array([[1, 2], [2, 3]])
# b = np.arange(4).reshape((2, 2))
# c = a * b
# c_dot = np.dot(a, b)
# print(a)
# print(c)
# print(c_dot)

# 随机生成2行5列的矩阵
a = np.random.random((2, 5))
print(a)
print(np.sum(a, axis=1))  # axis=1表示行
print(np.min(a, axis=0))  # axis=0表示列
print(np.max(a, axis=1))
