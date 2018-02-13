import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x**2


plt.figure()  # 在figure后面的是新的绘图窗口，独立显示绘图的图片
plt.plot(x, y1)  # 绘制出线条

plt.figure(num=3, figsize=(8, 5))  # 定义num表示第几个，figsize表示图片大小
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0,
         linestyle='--')  # 绘制颜色为红，宽度为1.0，样式为--的线条

plt.show()  # 显示出来
