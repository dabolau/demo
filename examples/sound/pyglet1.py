import pyglet

#需要配合avbin使用
#下载地址http://avbin.github.io/AVbin/Download.html
song = pyglet.media.load('jinggao.mp3')
song.play()
pyglet.app.run()
