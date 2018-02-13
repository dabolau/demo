from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/control', methods=['GET', 'POST'])
def control(k=None):
    if request.method == 'POST':
        k = request.form['k']
        print(k)
        return render_template('control.html',
                               method='POST',
                               k=k)

    if request.method == 'GET':
        k= request.args['k']
        print(k)
        return render_template('control.html',
                               method='GET',
                               k=k)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
