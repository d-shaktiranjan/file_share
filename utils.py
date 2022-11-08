import os
from flask import request
import socket
from platform import system


def getSizeWithUnit(sizeInByte):
    temp = sizeInByte
    unitList = ["Bytes", "KB", "MB", "GB"]
    count = 0
    while count < 3:
        if temp < 1000:
            break
        count += 1
        temp /= 1000
    return round(temp, 2), unitList[count]


def removeFile(fileName):
    try:
        os.remove("files/"+fileName)
        return True
    except:
        return False


def isHostDevice():
    ipAddress = request.remote_addr
    return ipAddress == "127.0.0.1"


def getIpAddress():
    if system() == "Linux":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip_address = s.getsockname()[0]
        s.close()
    else:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    return ip_address
