import pyaudio
import wave
import sys

CHUNK = 1024

wf = wave.open('ding.wav', 'rb')

# 定义 (1)
p = pyaudio.PyAudio()

# 打开文件 (2)
stream = p.open(
    format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True)

# 读取数据
data = wf.readframes(CHUNK)

# 播放 (3)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

# 停止 (4)
stream.stop_stream()
stream.close()

# 关闭 (5)
p.terminate()