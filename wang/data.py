import pandas as pd

data2014 = pd.read_excel("wang/14-19.xlsx")

data2014["城市"] = data2014["城市"].str.strip()
# print(type(data2014["城市"][0]))

data2020 = pd.read_excel("wang/2020.xlsx")
data2020["城市"] = data2020["城市"].str.strip()
# print(type(data2020["城市"][0]))
print(data2020["城市"])

# print(data2014.head)
# print(data2020.head)

final = pd.concat([data2014, data2020], axis=0)
final.sort_values(["城市", "年份"], inplace=True)
# print(final)
final.to_excel("wang/data.xlsx", index=False)
