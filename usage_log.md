.str.replace() 과 replace() 혼동해서 기능 차이 물어봄.

월 추출에 대한 질문.
답변|
df["주문일자"] = pd.to_datetime(df["주문일자"])
df["월"] = df["주문일자"].dt.month