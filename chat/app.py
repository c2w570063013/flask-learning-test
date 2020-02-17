from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    # print(jsonify({'ip': request.remote_addr}), 200)
    # print('======================='+request.remote_addr)
    print('Message: ' + msg)
    # msg = request.remote_addr + ': ' + msg
    send(msg, broadcast=True)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@app.route('/test')
def index2():
    return render_template('index2.html', async_mode=socketio.async_mode)


@app.route('/verify')
def verify():
    return render_template('verify.html')
    pass


if __name__ == '__main__':
    socketio.run(app)
