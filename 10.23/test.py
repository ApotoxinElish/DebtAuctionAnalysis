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

    time_series2 = list(set(time_series2))
    time_series2.sort(reverse=True)

    time_series.extend(time_series2)
    time_series = list(set(time_series))
    time_series.sort(reverse=True)
    # print(time_series)
    return time_series


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
    print("Rate:", list01.count(1) / len(list01))
    # return list01


def main():
    dai_data = readData()
    time_series = readTimeIndex()
    # print(time_series)

    for each in time_series:
        characterization(dai_data, each)

    # print("\nLeft Mean:", left_mean)
    # print("\nLeft Varance:", left_var)
    # print("\nRight Mean:", right_mean)
    # print("\nRight Varance:", right_var)

    convert01()
    # list01


if __name__ == "__main__":
    main()
