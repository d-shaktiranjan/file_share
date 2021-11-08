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
