import RPi.GPIO as GPIO
import time


def relay(i=0):
    # 设置针脚模式为（BOARD）
    GPIO.setmode(GPIO.BOARD)
    # 禁用警告
    GPIO.setwarnings(False)
    # 设置针脚
    PIN = 40
    # 设置针脚为输出模式
    GPIO.setup(PIN, GPIO.OUT)
    # 设置开关（0/1），0表示关，1表示开。
    INT = i

    # 开（闭合）
    if INT == 1:
        GPIO.output(PIN, GPIO.HIGH)  # 高电平输出
        print('power on')

    # 关（断开）
    if INT == 0:
        GPIO.output(PIN, GPIO.LOW)  # 低电平输出
        print('power off')

    # 延时5秒
    time.sleep(5)
    # 释放针脚
    GPIO.cleanup()


if __name__ == '__main__':
    relay(1)  # 开
    relay(0)  # 关
    relay(1)  # 开
