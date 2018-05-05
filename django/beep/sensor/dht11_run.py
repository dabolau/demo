import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests

# 初始化（GPIO）
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# 数据读取使用引脚（7）
instance = dht11.DHT11(pin=40)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

        name = '设备室01'
        location = '白居寺车场'
        temperature = result.temperature
        humidity = result.humidity

        # 网页地址
        url = 'http://localhost:8000/add'
        # 网页参数
        params = {
            'name': name,
            'location': location,
            'temperature': temperature,
            'humidity': humidity,
        }
        try:
            # 带参数的GET请求
            r = requests.get(url=url, params=params)
            # 获取返回状态
            print(r.status_code)
        except Exception as e:
            print(e)

    time.sleep(3)
