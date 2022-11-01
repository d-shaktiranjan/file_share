import os
from flask import request


def getSizeWithUnit(sizeInByte):
    temp = sizeInByte
    unitList = ["Byte", "KB", "MB", "GB"]
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
