import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#绘制数据

# data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# data=data.cumsum()

#矩阵数据
data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
data=data.cumsum()
print(data.head())
# data.plot()
# data.plot.scatter(x='A',y='B')
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()

