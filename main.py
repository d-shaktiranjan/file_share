from flask import Flask, render_template, send_file
import socket
from os import listdir, mkdir, path

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    fileList = listdir("files")
    sizeList = []
    for i in fileList:
        fileSize = path.getsize(f"files/{i}")
        sizeList.append(fileSize)
    return render_template("index.html", files=zip(fileList, sizeList))


@app.after_request
def header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route("/download/<string:fName>")
def download(fName):
    return send_file("files/"+fName, as_attachment=True)


if __name__ == "__main__":
    try:
        mkdir("files")
    except:
        pass
    app.run(host=ip_address, debug=True)
