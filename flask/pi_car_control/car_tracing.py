import RPi.GPIO as GPIO
import time


# 寻迹
def tracing():
    # 设置针脚模式为（BOARD）
    GPIO.setmode(GPIO.BOARD)
    # 禁用警告
    GPIO.setwarnings(False)
    # 设置针脚
    PIN = 40
    # 设置针脚为输出模式
    GPIO.setup(PIN, GPIO.IN)

    while True:
        if GPIO.input(PIN) == True:
            print('#1')
        else:
            print('#2')

        time.sleep(1)

    # 释放针脚
    GPIO.cleanup()


if __name__ == '__main__':
    tracing()
