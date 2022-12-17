import matplotlib.pyplot as plt
import numpy as np
import json

resultDict = {}
monthNumber = []
msgCount = []
inputFile = open("result.json", encoding="utf-8")
data = json.load(inputFile)
for i in data["messages"]:
    msgDate = i["date"][0:7]
    resultDict.setdefault(msgDate, 0)
    resultDict[msgDate] += 1
for i in sorted(resultDict):
        monthNumber.append(i)
        msgCount.append(resultDict[i])
x = np.array(monthNumber)
y = np.array(msgCount)


plt.barh(x,y, color="black")
plt.show()