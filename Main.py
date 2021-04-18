from flask import Flask, render_template, send_file
import socket
from os import listdir

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    fileList = listdir("files")
    return render_template("index.html", files=fileList)


@app.route("/download/<string:fName>")
def func(fName):
    return send_file("files/"+fName, as_attachment=True)


if __name__ == "__main__":
    app.run(host=ip_address)
