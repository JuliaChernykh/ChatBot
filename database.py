import pandas as pd
import random
data = pd.read_csv("DataBase.csv", header=None)
exc = []
for i in range(1, 28):
    exc.append((data[data[0] == i][2]).tolist())
def random_exc(n):
    tmp = exc[n-1]
    return tmp[random.randint(0, len(tmp)-1)]