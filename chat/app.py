from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True
socketio = SocketIO(app)

users = {}
sids = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/orginate')
def orginate():
    socketio.emit('server orginated', 'Something happened on the server!')
    return '<h1>Sent!</h1>'


@socketio.on('message from user', namespace='/messages')
def receive_message_from_user(message):
    print('USER MESSAGE: {}'.format(message))
    emit('from flask', message.upper(), broadcast=True)


@socketio.on('username', namespace='/private')
def receive_username(username):
    users[username] = request.sid
    sids[request.sid] = username


@socketio.on('private_message', namespace='/private')
def private_message(payload):
    recipient_session_id = users[payload['username']]
    data = {'message': payload['message'], 'username': sids[request.sid]}
    emit('new_private_message', data, room=recipient_session_id)


if __name__ == '__main__':
    socketio.run(app)
