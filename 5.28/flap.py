from black import diff
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tarpath = r"5.28/flap.csv"


def read():
    tarFile = pd.read_csv(tarpath)
    return tarFile


def dataProcess():
    target = read()

    target.dropna(subset=["win_or_lost"], inplace=True)
    print(target)

    theTime = pd.to_datetime(target.Time, format="%Y/%m/%d %H:%M:%S")
    # auctionStartBlockTime = pd.to_datetime(
    #     target.auction_start_block_time, format="%Y/%m/%d %H:%M:%S"
    # )
    exchangeRate = target.exchange_rate
    print(type(exchangeRate[3]))
    winRate = target.win_rate
    print(type(winRate[3]))
    winOrLost = target.win_or_lost
    print(type(winOrLost[3]))

    return

    # differ = takeBlockTime - auctionStartBlockTime
    # differ /= np.timedelta64(1, "m")
    # differ = differ.rename("differ")

    # startTime = auctionStartBlockTime  # .dt.strftime("%y-%m")
    # startTime = startTime.rename("start_time")

    # differDF = pd.concat([startTime, differ], axis=1)

    # differDF = (
    #     differDF.resample("W-Mon", on="start_time")
    #     .mean()
    #     .reset_index()
    #     .sort_values(by="start_time")
    # )
    # differDF.set_index("start_time", inplace=True)

    # differDF = differDF.groupby("start_time").mean()

    return differDF.sort_index()


def plotDraw():
    result = dataProcess()
    # print(result)

    # fig, ax = plt.subplots()
    # ax.bar(result.index, result.differ, 5)
    # # ax.plot(result.index, result.differ)
    # ax.set_title("liquidation2 time differ")
    # plt.show()

    # fig, ax = plt.subplots()
    # ax.bar(result.index, result.differ, 5)
    # # ax.plot(result.index, result.differ)
    # ax.set_title("liquidation2 time differ")
    # plt.show()




if __name__ == "__main__":
    plotDraw()
