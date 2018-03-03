# mjpg-streamer

1. 软件地址
> https://github.com/jacksonliam/mjpg-streamer

2. 编译和安装
> 必须安装cmake和libjpeg8-dev
```linux
sudo apt-get install cmake libjpeg8-dev
```

3. 简单的编译
```linux
cd mjpg-streamer-experimental
make
sudo make install
```

4. 使用方法
```linux
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
```

5. 预览方法
> 在浏览器中输入ip:8080
