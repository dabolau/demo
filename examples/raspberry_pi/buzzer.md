蜂鸣器控制
===

硬件线路连接方式
---

1.  树莓派选择（BOARD）模式
*  （2）引脚5V，电源，选择（红色）线连接
*  （6）引脚GND，接地，选择（黑色）线连接
*  （40）引脚GPIO，控制，选择（白色）线连接
2.  蜂鸣器（低电平触发）
*   (VCC)引脚，电源，连接红色线
*   (GND)引脚，接地，连接黑色线
*   (I/O)引脚，控制，连接白色线

演示代码
---

```python
import RPi.GPIO as GPIO
import time

def buzzer(i=0):
    # 设置针脚模式为（BOARD）
    GPIO.setmode(GPIO.BOARD)
    # 禁用警告
    GPIO.setwarnings(False)
    # 设置针脚
    PIN = 40
    # 嘀停，嘀停，嘀停，的形式蜂鸣
    if i == 0:
        for _i in range(1, 4):
            # 设置针脚为输出，蜂鸣器响
            GPIO.setup(PIN, GPIO.OUT)
            time.sleep(1)
            # 设置针脚为输入，蜂鸣器停
            GPIO.setup(PIN, GPIO.IN)
            # 延时1秒
            time.sleep(1)
            print(_i, time.time())
    # 嘀嗒，嘀嗒，嘀嗒，的形式蜂鸣
    if i == 1:
        for _i in range(1, 4):
            # 设置针脚为输出，蜂鸣器响
            GPIO.setup(PIN, GPIO.OUT)
            # 设置针脚输出低电平，蜂鸣器嘀响
            GPIO.output(PIN, GPIO.LOW)
            # 延时1秒
            time.sleep(1)
            # 设置针脚输出高电平，蜂鸣器嗒响
            GPIO.output(PIN, GPIO.HIGH)
            # 延时1秒
            time.sleep(1)
            print(_i, time.time())
    # 释放针脚
    GPIO.cleanup()

if __name__ == '__main__':
    buzzer()
```