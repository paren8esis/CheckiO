def checkio(data):
    newData = []
    for i in range(0, len(data)):
        if (data.count(data[i]) > 1):
            newData.append(data[i])
    return newData
