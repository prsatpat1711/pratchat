# socket_blueprint.py

from flask import Blueprint
from flask_socketio import SocketIO

socket_blueprint = Blueprint('socket', __name__)
socketio = SocketIO()

@socket_blueprint.route('/')
def index():
    return "Socket Blueprint"

@socketio.on('message', namespace='/socket')
def handle_message(message):
    print('received message: ' + message)
    socketio.emit('message', message, namespace='/socket')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/socket')
def handle_disconnect():
    print('Client disconnected')
