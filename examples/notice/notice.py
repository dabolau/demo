import requests
import time
import json
from playsound import playsound


#获取配置文件
def get_json(base_config):
    with open(base_config, 'r') as f:
        json_dict = json.load(f)
    return json_dict


#获取温度和湿度数据
def get_data(base_site):
    html = requests.get(base_site)
    html.encoding = 'utf-8'
    data = html.json()
    return data


if __name__ == '__main__':
    #获取配置文件
    gj = get_json('config.json')

    #获取配置文件中的数据
    base_url = gj['url']
    base_offset = gj['offset']
    base_site = base_url + base_offset
    base_mp3 = gj['mp3']
    base_location = gj['location']
    base_temperature = int(gj['temperature'])
    base_humidity = int(gj['humidity'])
    base_time = int(gj['time'])  #当前设置时间加5秒

    # 软件启动说明
    print('#' * 42)
    print('# 版权所有：重庆市轨道交通（集团）有限公司')
    print('# 开发人员：白居寺车场通信工班')
    print('# 联系电话：68004925')
    print('#' * 42)

    #时间延迟
    time.sleep(base_time)
    while True:
        print('#' * 42)

        #获取温度和湿度数据
        d = get_data(base_site)

        #显示温度和湿度数据
        print('编号：', d['id'])
        print('名称：', d['name'])
        print('位置：', d['location'])
        print('温度：', d['temperature'])
        print('湿度：', d['humidity'])
        print('时间：', d['create_time'])

        #传感器温度超过配置文件温度且传感器位置和配置文件位置相同语音警告
        if int(d['temperature']
               ) >= base_temperature and d['location'] == base_location:
            print('提示：', d['name'], '发生告警，请注意检查。')
            #播放告警提示音频
            playsound('jinggao.mp3')
            time.sleep(5)
        else:
            print('提示：', d['name'], '一切正常。')
            time.sleep(5)

        #时间延迟
        time.sleep(base_time)
