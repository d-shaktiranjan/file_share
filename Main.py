from flask import Flask, render_template
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=ip_address)
