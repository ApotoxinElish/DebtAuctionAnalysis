import pandas as pd
import matplotlib.pyplot as plt


def readData():
    data = pd.read_csv("new_list.csv")
    # print(data.head())
    return data


def plotData(data):
    plt.figure()
    plt.scatter(
        data.index,
        data.mean_ratio,
        s=20,
        edgecolor="black",
        c="darkorange",
        label="ratio",
    )
    # plt.xlabel("date_time")
    plt.ylabel("mean_ratio")
    plt.title("mean_ratio")
    plt.legend()
    plt.show()

    plt.figure()
    plt.scatter(
        data.index,
        data.var_ratio,
        s=20,
        edgecolor="black",
        c="darkorange",
        label="ratio",
    )
    # plt.xlabel("date_time")
    plt.ylabel("var_ratio")
    plt.title("var_ratio")
    plt.legend()
    plt.show()


def main():
    data = readData()
    plotData(data)


if __name__ == "__main__":
    main()
