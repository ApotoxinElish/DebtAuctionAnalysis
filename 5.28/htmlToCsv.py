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


def parseLine(line):
    pass


def main():
    content = readFileContent("5.28/flap.txt")

    offset = 0
    while True:
        line, offset = readEachLine(content, offset)
        if line == None:
            break
        # print(line)
        parseLine(line)
        break


if __name__ == "__main__":
    main()

# 6309
