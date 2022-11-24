import numpy as np
import pandas as pd
import pathlib
import math
import matplotlib.pyplot as plt

# pd.options.display.max_rows = 9999

def exchangeDataFrameColumn(df, column1, column2):
    i = list(df.columns)
    a, b = i.index(column1), i.index(column2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df

def main():
  #1.
  dataFrame = pd.read_csv(str(pathlib.Path(__file__).parent.resolve())+"\data\data.csv")
  print(dataFrame)
  
  # 2.
  # newdf = dataFrame.reset_index()
  # print(newdf)
  
  #3.
  # newdf.loc[dataFrame["Cabin"] == "C85", "Cabin"] = "C77"
  # print(newdf)
  
  #4.
  # columnNames = list(dataFrame.columns.values)
  # print(columnNames)
  # col_list= ['PassengerId', 'Survived', "Age", "SibSp", "Parch" , "Fare"]
  # dataFrame["sum"] = dataFrame[col_list].sum(axis=1)
  # # print(dataFrame)
  
  #5.
  # dataFrame = exchangeDataFrameColumn(dataFrame, "PassengerId","Fare")
  # dataFrame = dataFrame.sort_values(by=['Age'])
  # print(dataFrame)
  
  #6.
  # rowsCount = dataFrame.count()[0]
  # lowerBound = math.floor(rowsCount*5/100)  
  # dataFrame = dataFrame.drop(dataFrame.index[0:lowerBound])
  # rowsCount = dataFrame.count()[0]
  # upperBound = dataFrame.count()[0] - math.floor((rowsCount*5/100))
  # dataFrame = dataFrame.drop(dataFrame.index[upperBound-1:rowsCount-1])
  # print(dataFrame)
  
  #7.
  # averageAge = dataFrame["Age"].mean()
  # print(averageAge)
  # dataFrame["Age"] = dataFrame['Age'].fillna(averageAge)
  # print(dataFrame)
  # pieChart = dataFrame.loc[:200].plot.pie(y="Parch")
  # plt.show()
  
  #8.
  # dict1 = {
  #   "column_1": [123, 847, 374, 123, 123, 320, 320],
  #   "column_2": [503, 740, 451, 123, 340, 451, 320],
  #   "column_3": [543, 642, 127, 123, 340, 320, 320]
  # }
  # dataFrame1 = pd.DataFrame(dict1)
  
  # dict2 = {
  #   "column_4": [743, 512, 946],
  #   "column_5": [52, 12, 645],
  #   "column_6": [78, 123, 432]
  # }
  # dataFrame2 = pd.DataFrame(dict2)
  # dataFrame2ColumnNames = list(dataFrame2.columns.values)
  # for col in dataFrame2ColumnNames:
  #   dataFrame1 = dataFrame1.join(dataFrame2[col])
  # print(dataFrame1)
  # pieChart = dataFrame1.plot.bar(x='column_1', y='column_2', rot=0)
  # plt.show()
  
  #9.
  # hist = dataFrame.hist(column='Age', color='#1DB954')
  # plt.show()
  
  #10.
  # correlationMatrix = dataFrame1.corr(numeric_only=True)["column_1"]
  # print(correlationMatrix)


if __name__ == "__main__":
    main()
