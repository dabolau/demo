import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
# y = 2 * x + 1
y = x**2

plt.plot(x, y)  # 绘制出线条
plt.show()  # 显示出来
