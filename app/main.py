import socket

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Docker container Id: {socket.gethostname()} \n Hello world, my name is laitopez"
