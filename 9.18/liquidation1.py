import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tarpath = r"data/maker data dump/maker.liquidation.1.20220403.csv"


def read():
    tarFile = pd.read_csv(tarpath)
    return tarFile


def calTimeDiff(data):
    # print(data)
    tmin = data.tendTime.min()

    tmax = data.tendTime.max()
    dmax = data.dentTime.max()

    endT = max(tmax, dmax)
    # print(tmin)
    # print(endT)

    diff = endT - tmin
    diff /= np.timedelta64(1, "m")
    # print(diff)

    return (tmin, diff)


def checkYear(data):
    timeSeries = data.dropna(subset=["yearTime"])
    # print(timeSeries)
    yearSet = list(set(timeSeries.yearTime.to_list()))
    yearSet.sort()
    # yearSet.remove(NULL)
    # print(yearSet)
    # print(type(yearSet[0]))

    yearResult = []
    for i in yearSet:
        newData = timeSeries.loc[timeSeries["yearTime"] == i]
        # print(newData)
        yearResult.append(calTimeDiff(newData))

    return yearResult


def dataProcess(target):
    # dealTime = pd.to_datetime(target.deal_time, format="%Y/%m/%d %H:%M:%S")
    # kickTime = pd.to_datetime(target.kick_time, format="%Y/%m/%d %H:%M:%S")

    tendTime = pd.to_datetime(target.tend_time, format="%Y/%m/%d %H:%M:%S")
    dentTime = pd.to_datetime(target.dent_time, format="%Y/%m/%d %H:%M:%S")
    yearTime = tendTime.dt.strftime("%Y-%m-%d")
    pureData = {
        "liquidation_id": target.liquidation_id,
        "tendTime": tendTime,
        "dentTime": dentTime,
        "yearTime": yearTime,
    }
    pureData = pd.DataFrame(pureData)
    # print(pureData)
    # print(type(pureData.liquidation_id[0]))

    result = []
    ids = set(pureData.liquidation_id.to_list())
    for i in ids:  # range(1, 4991):
        data = pureData.loc[pureData["liquidation_id"] == i]
        # print(data)
        result.extend(checkYear(data))

    dfTime = pd.DataFrame(result, columns=["start", "duration"])
    dfTime.start = dfTime.start.dt.strftime("%Y-%m-%d")
    return dfTime
    # return

    # return

    # dealDiffer = dealTime - kickTime
    # dealDiffer /= np.timedelta64(1, "m")
    # dealDiffer = dealDiffer.rename("deal_differ")

    # tendDiffer = tendTime - kickTime
    # tendDiffer /= np.timedelta64(1, "m")
    # tendDiffer = tendDiffer.rename("tend_differ")

    # dentDiffer = dentTime - kickTime
    # dentDiffer /= np.timedelta64(1, "m")
    # dentDiffer = dentDiffer.rename("dent_differ")

    # startTime = kickTime  # .dt.strftime("%y-%m")

    # differDF = pd.concat([startTime, dealDiffer, tendDiffer, dentDiffer], axis=1)
    # differDF = (
    #     differDF.resample("W-Mon", on="kick_time")
    #     .mean()
    #     .reset_index()
    #     .sort_values(by="kick_time")
    # )
    # differDF.set_index("kick_time", inplace=True)

    # differDF = differDF.groupby("kick_time").mean()

    # return differDF.sort_index()


def plotDraw(result):
    fig, ax = plt.subplots()
    ax.bar(result.index, result.duration, 1)
    ax.set_title("liquidation1 deal time differ")
    plt.show()

    # fig, ax = plt.subplots()
    # ax.bar(result.index, result.tend_differ, 5)
    # ax.set_title("liquidation1 tend time differ")
    # plt.show()

    # fig, ax = plt.subplots()
    # ax.bar(result.index, result.dent_differ, 5)
    # ax.set_title("liquidation1 dent time differ")
    # plt.show()


def main():
    target = read()
    result = dataProcess(target)

    print(result)
    # return
    plotDraw(result)


if __name__ == "__main__":
    main()
