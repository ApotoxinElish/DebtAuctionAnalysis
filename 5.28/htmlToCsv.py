def readFileContent(fileName):
    with open(fileName) as file:
        content = file.read()
    return content


def readEachLine(content, offset):
    eachRowStart = content.find("row flip", offset)
    # print(content[eachRowStart])
    if eachRowStart == -1:
        return None, offset

    eachRowEnd = content.find("Info", eachRowStart) + 4
    # print(content[eachRowEnd])

    return content[eachRowStart:eachRowEnd], eachRowEnd


DataDict = {
    "Type": [],
    "Time": [],
    "ID": [],
    "lot": [],
    "bid": [],
    "Took Rate": [],
    "Rate": [],
    "Price": [],
    "from": [],
    "Link": [],
}


def parseLine(line):
    offset = line.find('">') + 2
    offsetB = line.find(" &gt;", offset)
    DataDict["Type"].append(line[offset:offsetB])

    offset = line.find("&gt; ", offsetB) + 5
    offsetB = line.find(" |", offset)
    DataDict["Time"].append(line[offset:offsetB])

    offset = line.find("ID: <b>", offsetB) + 7
    offsetB = line.find("</b>", offset)
    DataDict["ID"].append(line[offset:offsetB])

    offset = line.find("lot: ", offsetB) + 5
    if offset == 4:
        DataDict["lot"].append("")
        offset = offsetB
    else:
        offsetB = line.find(" |", offset)
        DataDict["lot"].append(line[offset:offsetB])

    offset = line.find("bid: ", offsetB) + 5
    if offset == 4:
        DataDict["bid"].append("")
        offset = offsetB
    else:
        offsetB = line.find(" |", offset)
        DataDict["bid"].append(line[offset:offsetB])

    offset = line.find("Took Rate: ", offsetB, offsetB + 10) + 11
    if offset == 10:
        DataDict["Took Rate"].append("")
        offset = offsetB
    else:
        offsetB = line.find(" |", offset)
        DataDict["Took Rate"].append(line[offset:offsetB])

    print(DataDict)


def main():
    content = readFileContent("5.28/flap.txt")

    offset = 0
    while True:
        line, offset = readEachLine(content, offset)
        if line == None:
            break
        print(line)
        parseLine(line)
        break


if __name__ == "__main__":
    main()

# 6309
