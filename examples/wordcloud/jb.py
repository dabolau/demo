import jieba as jb


# https://zhuanlan.zhihu.com/p/32891779
text = '李小璐给王思聪买了微博热搜'
# 强调特殊名词
jb.suggest_freq(('微博'), True)
jb.suggest_freq(('热搜'), True)
# 结果
result = jb.cut(text)
print(','.join(result))
