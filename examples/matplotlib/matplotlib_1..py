import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()


# plt.savefig('e.png') #保存到文件
plt.show()
