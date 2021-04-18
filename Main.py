from flask import Flask
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)
