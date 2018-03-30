from flask import Flask, request, render_template
from car import *


app = Flask(__name__)


@app.route('/')
def home():
    # 渲染页面
    return render_template('home.html')


@app.route('/control', methods=['GET', 'POST'])
def control(k=None):
    if request.method == 'POST':
        k = request.form['k']
        print(k)
        if k == 'w':
            print('前')
            go(0.1)
        elif k == 's':
            print('后')
            back(0.1)
        elif k == 'a':
            print('左')
            left(0.1)
        elif k == 'd':
            print('右')
            right(0.1)
        # 渲染页面
        return render_template('control.html',
                               method='POST',
                               k=k)

    if request.method == 'GET':
        k = request.args['k']
        print(k)
        if k == 'w':
            print('前')
        elif k == 's':
            print('后')
        elif k == 'a':
            print('左')
        elif k == 'd':
            print('右')
        # 渲染页面
        return render_template('control.html',
                               method='GET',
                               k=k)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
