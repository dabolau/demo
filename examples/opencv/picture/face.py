import cv2


filename = cv2.imread('9.jpeg')


# 人脸识别函数
def detect(img):
    # 声明变量，opencv的CascadeClassifier分类器训练
    # haarcascade_frontalface_default.xml可在官方github中下载
    face_cascade = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')
    # 将图片进行灰度处理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 进行实际的人脸检测，传递参数是scaleFactor和minNeighbor
    # 分别表示人脸检测过程中每次迭代时图像的压缩率和每个人脸矩形保留近邻数目的最小值
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # 依次提取faces变量中的值来画矩形
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 1)
    # 显示窗口和图片
    cv2.imshow('i', img)
    # 按任意键关闭窗口
    cv2.waitKey(0)


if __name__ == '__main__':
    detect(filename)
