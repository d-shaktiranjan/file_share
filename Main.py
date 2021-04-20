from flask import Flask, render_template, send_file
import socket
from os import listdir, stat, mkdir

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    fileList = listdir("files")
    sizeList = []
    for i in fileList:
        about = stat(f"files/{i}")
        sizeList.append(about.st_size/1000)
    return render_template("index.html", files=fileList, size=sizeList)


@app.route("/download/<string:fName>")
def func(fName):
    return send_file("files/"+fName, as_attachment=True)


if __name__ == "__main__":
    try:
        mkdir("files")
    except:
        pass
    app.run(host=ip_address, debug=True)
