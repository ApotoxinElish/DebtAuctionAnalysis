from matplotlib.pyplot import text
import pandas as pd


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
    # "Took Rate": [],
    "exchange_rate": [],
    "win_rate": [],
    "win_or_lost": [],
    "Rate": [],
    "Price": [],
    "from": [],
    "Link": [],
}


def parseLine(line):
    offset = line.find('">') + 2
    offsetB = line.find(" &gt;", offset)
    if line[offset:offsetB] in ["FILE", "RELY", "DENY"]:
        return
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

    offset = line.find("Took Rate: ", offsetB) + 11
    if offset == 10:
        # DataDict["Took Rate"].append("")
        DataDict["exchange_rate"].append("")
        DataDict["win_rate"].append("")
        DataDict["win_or_lost"].append("")
        offset = offsetB
    else:
        offsetB = line.find(" dai/mkr", offset)
        DataDict["exchange_rate"].append(line[offset:offsetB])

        offset = line.find(" (", offsetB) + 2
        offsetB = line.find(") ", offset)
        DataDict["win_rate"].append(line[offset:offsetB])

        # offsetB = line.find("<b ", offset)
        # tookRate = line[offset:offsetB]
        offset = line.find('">', offsetB) + 2
        offsetB = line.find(" ", offset)
        # tookRate += line[offset:offsetB]
        # DataDict["Took Rate"].append(tookRate)
        DataDict["win_or_lost"].append(line[offset:offsetB])

    offset = line.find("| ", offsetB) + 2
    offsetB = line.find("% |", offset) + 1
    if offsetB == 0:
        DataDict["Rate"].append("")
    else:
        DataDict["Rate"].append(line[offset:offsetB])

    offset = line.find("Price: ", offsetB) + 7
    offsetB = line.find(" |", offset)
    DataDict["Price"].append(line[offset:offsetB])

    offset = line.find("from: ", offsetB) + 6
    offsetB = line.find(" |", offset)
    DataDict["from"].append(line[offset:offsetB])

    offset = line.find('href="', offsetB) + 6
    offsetB = line.find('">', offset)
    DataDict["Link"].append(line[offset:offsetB])

    # print(DataDict)


def main():
    content = readFileContent("5.28/flap.txt")

    offset = 0
    while True:
        line, offset = readEachLine(content, offset)
        if line == None:
            break
        # print(line)
        parseLine(line)
        # break

    data = pd.DataFrame(DataDict)
    data["ID"] = data["ID"].astype(int)
    data["Time"] = pd.to_datetime(data["Time"], format="%d %b %Y, %H:%M:%S")
    data.sort_values(["ID", "Time", "Type"], inplace=True)
    data.to_csv("5.28/flap.csv", index=False)

    # data = pd.read_csv("data.csv")

    # data.to_csv("data.csv", index=False)


if __name__ == "__main__":
    main()

# 6309
