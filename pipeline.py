import pandas as pd
pd.set_option("display.width", 180)

df = pd.read_csv("RAW_DATA.csv", encoding="cp949")

#print(df.shape)
#print(df.info())
"""
(500, 5)
<class 'pandas.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   주문일자    500 non-null    str  
 1   상품명     500 non-null    str  
 2   카테고리    500 non-null    str  
 3   단가      500 non-null    str  
 4   수량      500 non-null    int64
dtypes: int64(1), str(4)
memory usage: 19.7 KB
None
"""

df["단가"] = (pd.to_numeric(df["단가"].astype(str).str.replace(",","",regex=False), errors = "coerce").astype("Int64"))
df["매출액"] = df["단가"]*df["수량"]


df["주문일자"] = pd.to_datetime(df["주문일자"])
df["월"] = df["주문일자"].dt.month
report = df.groupby(["월", "카테고리"])["매출액"].agg(
    총매출 = "sum", 평균매출="mean", 거래건수="count")
report = report.reset_index()


by_cat = (df.groupby("카테고리")["매출액"].sum().reset_index())
sorted_df = by_cat.sort_values("매출액", ascending=False)


with pd.ExcelWriter("Montly_Report.xlsx", engine="openpyxl") as writer:
    report.to_excel(writer, sheet_name="월별카테고리요약", index=False)
    by_cat.to_excel(writer, sheet_name="카테고리별합계", index=False)

원본합계 = df["매출액"].sum()
집계합계 = report["총매출"].sum()
assert 원본합계 == 집계합계
print("*****완료*****")