import pandas as pd

data2014 = pd.read_excel("wang/14-19.xlsx")
data2020 = pd.read_excel("wang/2020.xlsx")

print(data2014.head)
# print(data2020.head)

final = pd.concat([data2014, data2020], axis=0)
# print(final)
final.to_excel("data.xlsx")
