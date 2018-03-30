# 导入模块（GPIO）
import RPi.GPIO as GPIO
import time


# 设置模式（GPIO）
GPIO.setmode(GPIO.BOARD)


# 定义通信接口（GPIO）
INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15


# 设置接口为输出（GPIO）
def init():
    GPIO.setup(INT1, GPIO.OUT)
    GPIO.setup(INT2, GPIO.OUT)
    GPIO.setup(INT3, GPIO.OUT)
    GPIO.setup(INT4, GPIO.OUT)


# 设置接口为不输出（GPIO）
def stop():
    GPIO.output(INT1, False)
    GPIO.output(INT2, False)
    GPIO.output(INT3, False)
    GPIO.output(INT4, False)


# 根据树莓派和电机控制器（L298N）接线输出高低电平(前进)
def go(sleep_time):
    init()
    GPIO.output(INT1, GPIO.HIGH)
    GPIO.output(INT2, GPIO.LOW)
    GPIO.output(INT3, GPIO.HIGH)
    GPIO.output(INT4, GPIO.LOW)
    time.sleep(sleep_time)
    stop()


# 根据树莓派和电机控制器（L298N）接线输出高低电平（后退）
def back(sleep_time):
    init()
    GPIO.output(INT1, GPIO.LOW)
    GPIO.output(INT2, GPIO.HIGH)
    GPIO.output(INT3, GPIO.LOW)
    GPIO.output(INT4, GPIO.HIGH)
    time.sleep(sleep_time)
    stop()


# 根据树莓派和电机控制器（L298N）接线输出高低电平（左转）
def left(sleep_time):
    init()
    GPIO.output(INT1, GPIO.HIGH)
    GPIO.output(INT2, GPIO.LOW)
    GPIO.output(INT3, GPIO.LOW)
    GPIO.output(INT4, GPIO.HIGH)
    time.sleep(sleep_time)
    stop()


# 根据树莓派和电机控制器（L298N）接线输出高低电平（右转）
def right(sleep_time):
    init()
    GPIO.output(INT1, GPIO.LOW)
    GPIO.output(INT2, GPIO.HIGH)
    GPIO.output(INT3, GPIO.HIGH)
    GPIO.output(INT4, GPIO.LOW)
    time.sleep(sleep_time)
    stop()


# go(0.1)
# stop()
# back(0.1)
# stop()
# left(0.1)
# stop()
# right(0.1)
# stop()


# 释放接口（GPIO）
GPIO.cleanup()
