##############################
# 版权归作者所有
# 作者：刘毅
# 日期：20171128
# 版本号：1.1
##############################
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 7
instance = dht11.DHT11(pin=7)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        
        name = '通信设备室'
        location = '白居寺'
        value1 = result.temperature
        value2 = result.humidity

        # 网页地址
        url = 'http://localhost:8000/add'
        # 网页参数
        params = {'name': name, 'location': location,
                  'value1': value1, 'value2': value2}
        # 带参数的GET请求
        r = requests.get(url=url, params=params)
        # 获取返回状态
        print(r.status_code)

    time.sleep(1)
