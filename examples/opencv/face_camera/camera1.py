# 导入开发框架
import cv2

# 打开摄像头
capture = cv2.VideoCapture(0)
# 准备人脸模型
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 创建一个窗口
cv2.namedWindow('camera')
# 实时检测摄像头人脸
while True:
    # 读取摄像头画面（图片）
    ret, frame = capture.read()
    # 将图片变为灰色（灰色图片一个颜色，彩色图片三个颜色）
    # 内存：颜色越少占用内存越少，颜色越多占用内存越多
    # 例如：灰色图片识别人脸（1秒）彩色图片识别人脸（5秒）
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 检测图片上的人脸，返回多张人脸
    faces = face.detectMultiScale(gray, 1.1, 3, 0, (100, 100))
    # 在图片上标记人脸
    # 标记：三角形，长方形，正方形，圆形等。。。
    # 注意：返回值为（坐标）
    for (x, y, w, h) in faces:
        # 标记人脸
        # 参数一：标记图片
        # 参数二：起点坐标
        # 参数三：结束位置
        # 参数四：标记图片颜色
        # 参数五：线宽（边框线条粗细）
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    # 显示图片
    cv2.imshow('face', frame)
    # 暂停窗口
    if cv2.waitKeyEx(5) & 0xFF == ord('q'):
        break

# 释放资源
capture.release()
# 关闭窗口
cv2.destroyAllWindows()