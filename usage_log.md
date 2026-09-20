.str.replace() 과 replace() 혼동해서 기능 차이 물어봄.

월 추출에 대한 질문.
답변|
df["주문일자"] = pd.to_datetime(df["주문일자"])
df["월"] = df["주문일자"].dt.month

카테고리별 합계를 할 때 카테고리의 이름이 사라지는 문제
-> DataFrame으로 바꾸는 것 (reset_index())
rest_index() 설명 - 인덱스로 올라가 있는 값을(카테고리) 다시 일반 열로 내려주는 함수