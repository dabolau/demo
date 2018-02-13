import numpy as np
import PIL.Image as image
import jieba as jb
import wordcloud as wc
import matplotlib.pyplot as plt

# 加载词云内容
with open('wikipedia.txt', 'r') as f:
    mytext = f.read()

# 分割词云内容，用空格隔开
mytext = ' '.join(jb.cut(mytext))

# 加载背景图片
wc_background = np.array(image.open('wikipedia.jpg'))
# 忽略要显示的词
ts = set(['编辑'])
# 绘制词云
wcs = wc.WordCloud(background_color='black',  # 背景颜色
                   mask=wc_background,  # 背景图片
                   stopwords=ts,  # 忽略要显示的词
                   max_words=200,  # 显示最大词数
                   font_path='simsun.ttf',  # 使用字体
                   min_font_size=4,  # 最小字体
                   max_font_size=300,  # 最大字体
                   width=400)  # 图片宽度
# 生成图片
wcs.generate(mytext)
# 保存图片
wcs.to_file('wc.png')
