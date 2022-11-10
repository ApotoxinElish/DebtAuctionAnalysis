import pandas as pd
import matplotlib.pyplot as plt


def readData():
    dai_data = pd.read_csv("prices_jp/prices.dai.2019.by_minute.20220221.csv")

    dai_data = pd.concat(
        [dai_data, pd.read_csv("prices_jp/prices.dai.2020.by_minute.20220221.csv")],
        axis=0,
    )
    dai_data = pd.concat(
        [dai_data, pd.read_csv("prices_jp/prices.dai.2021.by_minute.20220221.csv")],
        axis=0,
    )
    dai_data = pd.concat(
        [dai_data, pd.read_csv("prices_jp/prices.dai.2022.by_minute.20220221.csv")],
        axis=0,
    )
    dai_data.date_time = pd.to_datetime(dai_data.date_time, format="%Y/%m/%d %H:%M:%S")

    # print(data.head())
    return dai_data


def readTimeIndex():
    time_data = pd.read_csv("maker.liquidation.2.20220403.csv")
    time_series = pd.to_datetime(time_data.take_block_time, format="%Y/%m/%d %H:%M:%S")

    time_data2 = pd.read_csv("maker.liquidation.1.20220403.csv")
    time_series2 = pd.to_datetime(time_data2.deal_time, format="%Y/%m/%d %H:%M:%S")

    # print(time_series.head())
    # print(type(time_series))
    time_series = list(set(time_series))
    time_series.sort(reverse=True)
    print(len(time_series))
    time_series2 = list(set(time_series2))
    time_series2.sort(reverse=True)

    # time_series.extend(time_series2)
    # time_series = list(set(time_series))
    # time_series.sort(reverse=True)
    # print(time_series)
    return time_series2, len(time_series)


left_mean = []
left_var = []
right_mean = []
right_var = []


def characterization(dai_data, time_center):
    center_diff = pd.Timedelta("6 hours")
    left_center = time_center - center_diff
    right_center = time_center + center_diff
    # centers = [left_center, right_center]

    delta = pd.Timedelta("4.5 hours")

    left_usefuldata = dai_data.loc[
        (left_center - delta < dai_data.date_time)
        & (dai_data.date_time < left_center + delta)
    ]
    right_usefuldata = dai_data.loc[
        (right_center - delta < dai_data.date_time)
        & (dai_data.date_time < right_center + delta)
    ]

    if pd.notnull(left_usefuldata.dai.mean()):
        left_mean.append(left_usefuldata.dai.mean())
        left_var.append(left_usefuldata.dai.var())
        right_mean.append(right_usefuldata.dai.mean())
        right_var.append(right_usefuldata.dai.var())


def convert01():
    list01 = []
    for i in range(len(left_mean)):
        if left_mean[i] > 1:
            if left_mean[i] - right_mean[i] > 0:
                list01.append(1)
            elif left_mean[i] - right_mean[i] < 0:
                list01.append(0)
        elif left_mean[i] < 1:
            if left_mean[i] - right_mean[i] > 0:
                list01.append(0)
            elif left_mean[i] - right_mean[i] < 0:
                list01.append(1)
    # print("Rate:", list01.count(1) / len(list01))
    return list01


def ratio(list1):
    listMeanRatio = []
    listVarRatio = []
    for i in range(len(left_mean)):
        listMeanRatio.append(((left_mean[i] - right_mean[i])))
        listVarRatio.append(((left_var[i] / right_var[i])))
    dataframe = pd.DataFrame(
        {"MeanRatio": listMeanRatio, "VarRatio": listVarRatio, "Label": list1}
    )
    dataframe.to_csv("ratio.csv", index=False, sep=",")


def show(length):
    data = pd.read_csv("ratio.csv")
    data0 = data.loc[data["Label"] == 0]
    data1 = data.loc[data["Label"] == 1]
    plt.figure()
    plt.scatter(
        data0.index,
        data0.MeanRatio,
        s=1,
        c="b",
        label="ratio",
    )
    plt.scatter(
        data1.index,
        data1.MeanRatio,
        s=1,
        c="r",
        label="ratio",
    )
    plt.axhline(y=0, color="black", linewidth=0.5, linestyle="-")
    plt.axvline(x=length, color="black", linewidth=0.5, linestyle="-")
    plt.ylabel("Meanratio")
    plt.title("mean_ratio")
    plt.legend()
    plt.show()

    plt.figure()
    plt.scatter(
        data0.index,
        data0.VarRatio,
        s=1,
        c="b",
        label="ratio",
    )
    plt.scatter(
        data1.index,
        data1.VarRatio,
        s=1,
        c="r",
        label="ratio",
    )
    plt.axhline(y=0, color="black", linewidth=0.5, linestyle="-")
    plt.axvline(x=length, color="black", linewidth=0.5, linestyle="-")
    # plt.xlabel("date_time")
    plt.ylabel("var_ratio")
    plt.title("var_ratio")
    plt.legend()
    plt.show()
    plt.show()


def main():
    liquidaiton_1 = 0.27676240208877284
    liquidation_2 = 0.3769309989701339
    liquidaiton_1_2 = 0.34859675036927623
    dai_data = readData()
    time_series, length = readTimeIndex()
    print(time_series)

    for each in time_series:
        characterization(dai_data, each)

    # print("\nLeft Mean:", left_mean)
    # print("\nLeft Varance:", left_var)
    # print("\nRight Mean:", right_mean)
    # print("\nRight Varance:", right_var)
    list1 = convert01()
    ratio(list1)
    show(length)


if __name__ == "__main__":
    main()
