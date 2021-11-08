def getSizeWithUnit(sizeInByte):
    temp = sizeInByte
    unitList = ["Byte", "KB", "MB", "GB"]
    count = 0
    while temp > 1024:
        count += 1
        if temp < 1024 or count == 3:
            break
        temp /= 1024
    return round(temp, 2), unitList[count]
