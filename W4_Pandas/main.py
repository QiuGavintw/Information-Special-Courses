# 載入與檢視資料表內容
import pandas as pd
df = pd.read_csv('students.csv')
# 語法範例：預覽前五筆資料
print(df.head(10))
print("數學成績平均值：", df["math"].mean())  # 計算數學成績平均值
print("數學成績大於80的學生：")
print(df[ df["math"] > 80])  # 篩選數學成績大於80的學生
