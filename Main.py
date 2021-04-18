from flask import Flask, render_template
import socket
from os import listdir

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    fileList = listdir("files")
    return render_template("index.html", files=fileList)


if __name__ == "__main__":
    app.run(host=ip_address)
