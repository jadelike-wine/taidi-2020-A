# coding=gbk
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets.samples_generator import make_blobs

year = pd.read_csv('year.csv', encoding='GBK')
k = pd.read_csv('test2.csv', encoding='GBK')
x2 = k.iloc[:, :].values
x = year.iloc[:, :-1].values
y = year.iloc[:, 6].values
model = LogisticRegression()
model.fit(x, y)
y2 = model.predict_proba(x2)
end=list()
for i in range(3466):
    if y2[i][0] > y2[i][1]:
        end.append(0)
    else:
        end.append(1)
np.savetxt('true.txt', end)
print("ok")
##Probability of 0 and 1 respectively
