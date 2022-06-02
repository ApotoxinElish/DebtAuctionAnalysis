import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tarpath = r"5.27/maker.liquidation.surplus.20220403.csv"


def read():
    tarFile = pd.read_csv(tarpath)
    return tarFile


kick_block_number = []


def dataProcess():
    target = read()

    target.kick_time = pd.to_datetime(target.kick_time, format="%m/%d/%Y %H:%M:%S")
    print(type(target.kick_time[0]))
    target.sort_values(["kick_time", "surplus_auction_id"], inplace=True)
    id = target.surplus_auction_id
    kickBlockNumber = target.kick_block

    lastid = id[0]
    lastindex = 0
    # result = []
    for index in range(len(id) + 1):
        if index == len(id) or id[index] != lastid:
            if index < len(id) and id[index] < lastid:
                print(index + 2)
            # kick_time = kickTime[lastindex].strftime("%Y-%m-%d")

            # deal_kick = dealTime[index - 1] - kickTime[lastindex]
            # deal_kick /= np.timedelta64(1, "h")

            # deal_dent = dealTime[index - 1] - dentTime[lastindex]
            # deal_dent /= np.timedelta64(1, "h")

            # lot_start = dentLot[lastindex]
            # lot_ent = dentLot[index - 1]
            # lot_differ = lot_start - lot_ent

            # result.append((lastid, deal_kick, lot_differ, lot_ent))

            if index != len(id):
                kick_block_number.append(
                    kickBlockNumber[index] - kickBlockNumber[lastindex]
                )

                lastid = id[index]
                lastindex = index

    # resultDataFrame = pd.DataFrame(
    #     result,
    #     columns=["id", "deal_kick", "lot_differ", "lot_end"],
    # )
    # resultDataFrame.set_index("id", drop=True, inplace=True)

    # return resultDataFrame


def plotDraw():
    result = dataProcess()

    # fig, ax = plt.subplots()
    # ax.plot(result.index, result.deal_kick)
    # ax.set_title("deal - kick")
    # plt.show()

    # fig, ax = plt.subplots()
    # ax.plot(result.index, result.lot_differ)
    # ax.set_title("lot_differ")
    # plt.show()

    # fig, ax = plt.subplots()
    # ax.plot(result.index, result.lot_end)
    # ax.set_title("lot_end")
    # plt.show()

    fig, ax = plt.subplots()
    ax.scatter(np.arange(1, len(kick_block_number) + 1), kick_block_number)
    print(len(kick_block_number))
    ax.set_title("kick_block")
    plt.show()


if __name__ == "__main__":
    plotDraw()
