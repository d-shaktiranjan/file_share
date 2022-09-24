from flask import Flask, render_template, send_file, redirect
import socket
from os import listdir, mkdir, path
from utils import getSizeWithUnit, removeFile

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    fileList = listdir("files")
    sizeList = []
    units = []
    for i in fileList:
        fileSize = path.getsize(f"files/{i}")
        sizeWithUnit = getSizeWithUnit(fileSize)
        sizeList.append(sizeWithUnit[0])
        units.append(sizeWithUnit[1])
    return render_template("index.html", files=zip(fileList, sizeList, units))


@app.after_request
def header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route("/download/<string:fName>")
def download(fName):
    return send_file("files/"+fName, as_attachment=True)


@app.route("/delete/<string:fName>")
def delete(fName):
    removeFile(fName)
    return redirect("/")


if __name__ == "__main__":
    try:
        mkdir("files")
    except:
        pass
    app.run(host=ip_address, debug=True)
