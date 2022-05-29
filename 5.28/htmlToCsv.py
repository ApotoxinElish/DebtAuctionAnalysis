def readFileContent(fileName):
    with open(fileName) as file:
        content = file.read()
    return content


def readEachLine(content):
    eachRowStart = content.find("row flip")
    # print(content[eachRowStart])
    if eachRowStart == -1:
        return None

    eachRowEnd = content.find("Info", eachRowStart) + 4
    # print(content[eachRowEnd])

    return content[eachRowStart:eachRowEnd]


def main():
    content = readFileContent("5.28/flap.txt")

    offset = 0
    while True:
        line = readEachLine(content)
        if line == None:
            break
        print(line)
        # break


if __name__ == "__main__":
    main()

# 6309
