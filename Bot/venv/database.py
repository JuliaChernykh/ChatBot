import pandas as pd
data = pd.read_csv("DataBase.csv", header=None)
print(data)
print(data[data[1] == 1][2])