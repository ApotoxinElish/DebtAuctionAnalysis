import pandas as pd

data2014 = pd.read_excel("wang/14-19 工资.xlsx")
# print(data2014.head)
data2014 = data2014[~data2014["年份"].isin([2020])]
data2014["城市"] = data2014["城市"].str.strip()
# print(type(data2014["城市"][0]))

data2020 = pd.read_excel("wang/20 工资.xlsx")
# print(data2020.head)
# print(data2020["城市"])
data2020["城市"] = data2020["城市"].str.strip()
data2020.insert(0, "年份", [2020 for i in range(len(data2020))])
# print(type(data2020["城市"][0]))


# print(data2014.head)
# print(data2020.head)

df_mapping = pd.DataFrame(data2020["城市"])
sort_mapping = df_mapping.reset_index().set_index("城市")
# print(sort_mapping)

final = pd.concat([data2014, data2020], axis=0)


final["size_num"] = final["城市"].map(sort_mapping["index"])
final.sort_values(["size_num", "年份"], inplace=True)
final.drop("size_num", axis=1, inplace=True)
# print(final)
final.to_excel("wang/工资.xlsx", index=False)
