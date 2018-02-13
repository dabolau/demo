继电器控制
===

硬件线路连接方式
---

1.  树莓派选择（BOARD）模式
*  （2）引脚5V，电源，选择（红色）线连接
*  （6）引脚GND，接地，选择（黑色）线连接
*  （40）引脚GPIO，控制，选择（白色）线连接
2.  继电器接入（高电平时常开闭合，常闭断开，低电平时常开断开，常闭闭合，注意是什么电平触发）
*   (VCC)引脚，电源，连接红色线
*   (GND)引脚，接地，连接黑色线
*   (IN)引脚，控制，连接白色线
3.  继电器接出
*   (NO)引脚，常开，连接黑色线
*   (COM)引脚，公共端，连接灰色线
*   (NC)引脚，常闭，连接白色线
4.  电源（电池盒）
*   正极，连接继电器(COM)公共端灰色线
*   负极，连接发光二极管一引脚，另一引脚连接继电器(NO)常开黑色线，注意二极管的引脚正反

演示代码
---

```python
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
```