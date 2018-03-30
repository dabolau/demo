import RPi.GPIO as GPIO
import time


def checkdist():
    # 发出触发信号
    GPIO.output(2, GPIO.HIGH)
    # 保持10us以上（我选择15us）
    time.sleep(0.000015)
    GPIO.output(2, GPIO.LOW)
    while not GPIO.input(3):
        pass
    # 发现高电平时开时计时
    t1 = time.time()
    while GPIO.input(3):
        pass
    # 高电平结束停止计时
    t2 = time.time()
    # 返回距离，单位为米
    return (t2 - t1) * 340 / 2


GPIO.setmode(GPIO.BCM)
# 第3号针，GPIO2
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)
# 第5号针，GPIO3
GPIO.setup(3, GPIO.IN)

time.sleep(2)
try:
    while True:
        print ('Distance: %0.2f m' % checkdist())
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
