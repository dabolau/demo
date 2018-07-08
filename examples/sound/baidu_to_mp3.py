from aip import AipSpeech
""" 你的百度 APPID AK SK
https://console.bce.baidu.com/ai/#/ai/speech/app/list       应用列表
http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top         API
"""
APP_ID = '9288864'
API_KEY = '7OOA9UFvHwC3pplzPZnqQ9pF'
SECRET_KEY = '4ea30a42379528355abb0fa6e31516a2'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
text = input('请输入要转换为语音的文本：')
result = client.synthesis(text, 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.wav', 'wb') as f:
        f.write(result)