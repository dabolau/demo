import multiprocessing as mp


# 分配共享内存
# 其中字符d参考下面的地址详细说明
# https://docs.python.org/3.5/library/array.html?highlight=array#module-array
value = mp.Value('d', 1)
array = mp.Array('i', [1, 2, 3])  # 只能是一维
