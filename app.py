from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
from gevent import pywsgi

from models.service import *

app = Flask(__name__)
app.secret_key = '021104'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def login():
    username = request.form.get('username')
    session['username'] = username
    return render_template('chat.html', username=username)

@socketio.on('message')
def handle_message(data):
    message = data['msg']

    sentiment_analyzer = SentimentAnalyzer()
    chatglm = ChatGLM()
    response = generate_emotional_reply(message, sentiment_analyzer, chatglm)
    
    emit('response', {'msg': response, 'username': session['username']}, broadcast=True)

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    print('Server running at http://127.0.0.1:5000/')
    server.serve_forever()