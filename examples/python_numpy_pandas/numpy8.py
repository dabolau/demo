import numpy as np

a = np.arange(4)
print(a)
b = a
c = a
d = b
a[0] = 11
print(a)
print(b is a)
print(c)
print(d)

e = a.copy()  # 深度拷贝，e就不是a了，但是内容是一样的。
print(e is a)
