import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tarpath = r"5.27/maker.liquidation.debt.20220403.csv"


def read():
    tarFile = pd.read_csv(tarpath)
    return tarFile


kick_block_number = []


def dataProcess():
    target = read()

    id = target.debt_auction_id
    dealTime = pd.to_datetime(target.deal_time, format="%Y/%m/%d %H:%M:%S")
    kickTime = pd.to_datetime(target.kick_time, format="%Y/%m/%d %H:%M:%S")
    # dentTime = pd.to_datetime(target.dent_time, format="%Y/%m/%d %H:%M:%S")
    dentLot = target.dent_lot
    kickBlockNumber = target.kick_block_number

    lastid = id[0]
    lastindex = 0
    result = []
    for index in range(len(id) + 1):
        if index == len(id) or id[index] != lastid:
            # kick_time = kickTime[lastindex].strftime("%Y-%m-%d")

            deal_kick = dealTime[index - 1] - kickTime[lastindex]
            deal_kick /= np.timedelta64(1, "h")

            # deal_dent = dealTime[index - 1] - dentTime[lastindex]
            # deal_dent /= np.timedelta64(1, "h")

            lot_start = dentLot[lastindex]
            lot_ent = dentLot[index - 1]
            lot_differ = lot_start - lot_ent

            result.append((lastid, deal_kick, lot_differ, lot_ent))

            if index != len(id):
                kick_block_number.append(
                    kickBlockNumber[index] - kickBlockNumber[lastindex]
                )

                lastid = id[index]
                lastindex = index

    resultDataFrame = pd.DataFrame(
        result,
        columns=["id", "deal_kick", "lot_differ", "lot_end"],
    )
    resultDataFrame.set_index("id", drop=True, inplace=True)

    return resultDataFrame


def plotDraw():
    result = dataProcess()

    fig, ax = plt.subplots()
    ax.plot(result.index, result.deal_kick)
    ax.set_title("deal - kick")
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(result.index, result.lot_differ)
    ax.set_title("lot_differ")
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(result.index, result.lot_end)
    ax.set_title("lot_end")
    plt.show()

    fig, ax = plt.subplots()
    ax.scatter(np.arange(1, 106), kick_block_number)
    ax.set_title("kick_block_number")
    plt.show()


if __name__ == "__main__":
    plotDraw()
