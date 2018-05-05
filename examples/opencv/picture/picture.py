import cv2


# 根据路径读取图片
img = cv2.imread('9.jpeg')
# 显示窗口名称和图片
cv2.imshow('i', img)
# 键盘出发事件，释放窗口
cv2.waitKey(0)
