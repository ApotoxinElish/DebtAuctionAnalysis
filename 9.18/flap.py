from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tarpath = r"flap.csv"


def read():
    tarFile = pd.read_csv(tarpath)
    return tarFile


def dataProcess():
    target = read()

    target.dropna(subset=["win_or_lost"], inplace=True)
    # print(target)

    target.loc[target["win_or_lost"] == "Won!", "win_or_lost"] = 1
    target.loc[target["win_or_lost"] == "Lost", "win_or_lost"] = -1

    return target

    theTime = pd.to_datetime(target.Time, format="%Y/%m/%d %H:%M:%S")
    # auctionStartBlockTime = pd.to_datetime(
    #     target.auction_start_block_time, format="%Y/%m/%d %H:%M:%S"
    # )

    exchangeRate = pd.to_numeric(target["exchange_rate($)"])
    print(type(exchangeRate[3]))
    winRate = pd.to_numeric(target["win_rate(%)"])
    print(type(winRate[3]))
    winOrLost = target.win_or_lost
    print(type(winOrLost[3]))

    # return

    # differ = takeBlockTime - auctionStartBlockTime
    # differ /= np.timedelta64(1, "m")
    # differ = differ.rename("differ")

    # startTime = auctionStartBlockTime  # .dt.strftime("%y-%m")
    # startTime = startTime.rename("start_time")

    exchangeRateAverage = pd.concat([theTime, exchangeRate], axis=1)

    exchangeRateAverage = (
        exchangeRateAverage.resample("W-Mon", on="Time")
        .mean()
        .reset_index()
        .sort_values(by="Time")
    )
    exchangeRateAverage.set_index("Time", inplace=True)

    # differDF = differDF.groupby("start_time").mean()

    winRateDF = pd.concat([theTime, winRate], axis=1)
    winRateDF.set_index("Time", inplace=True)

    winOrLostDF = pd.concat([theTime, winOrLost], axis=1)

    winDF = winOrLostDF.loc[winOrLostDF["win_or_lost"] == "Won!"]
    winDF = winDF.reset_index(drop=True)
    winDF.win_or_lost = pd.Series([1 for i in range(len(winDF))])
    winDF = (
        winDF.resample("W-Mon", on="Time").sum().reset_index().sort_values(by="Time")
    )
    winDF.set_index("Time", inplace=True)
    print(winDF)

    lostDF = winOrLostDF.loc[winOrLostDF["win_or_lost"] == "Lost"]
    lostDF = lostDF.reset_index(drop=True)
    lostDF.win_or_lost = pd.Series([1 for i in range(len(lostDF))])
    lostDF = (
        lostDF.resample("W-Mon", on="Time").sum().reset_index().sort_values(by="Time")
    )
    lostDF.set_index("Time", inplace=True)
    print(lostDF)

    return exchangeRateAverage, winRateDF, (winDF, lostDF)  # winAndLost


def plotDraw():
    result = dataProcess()
    # result = dataProcess()
    # print(result)

    fig, ax = plt.subplots()
    ax.bar(result["ID"], result["exchange_rate($)"], 5)
    # ax.plot(result.index, result.differ)
    ax.set_title("Exchange Rate Average ($ dai/mkr)")
    plt.show()

    fig, ax = plt.subplots()
    ax.scatter(result["ID"], result["win_rate(%)"], 5)
    ax.plot(result["ID"], [0 for i in range(len(result))], color="red")
    # ax.plot(result.index, result.differ)
    ax.set_title("Win Rate (%)")
    plt.show()

    fig, ax = plt.subplots()
    ax.scatter(result["ID"], result["win_or_lost"], 5)
    # ax.bar(winOrLost[1].index, -winOrLost[1]["win_or_lost"], 5)
    # ax.plot(result.index, result.differ)
    ax.set_title("Win Or Lost")
    # plt.legend(["Won!", "Lost"])
    plt.show()


if __name__ == "__main__":
    plotDraw()
