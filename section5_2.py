import pandas as pd
product = pd.read_excel(r"C:\Users\JSS\python_excel\source\chapter05\식자재 주문.xlsx", sheet_name = "product")
order = pd.read_excel(r"C:\Users\JSS\python_excel\source\chapter05\식자재 주문.xlsx", sheet_name = "order")

product
order

mapping = {"1": "청주", "2": "대구", "3": "광주"}
product["공장"] = product["제품코드"].str[4].map(mapping)
product.head()

# product.set_index("제품코드", inplace = True)
# order.set_index("제품코드", inplace = True)
# order["제품명"] = product["제품명"]
# order["단가"] = product["단가"]
# order["주문금액"] = order["주문수량"] * order["단가"]
# order

# order.reset_index(inplace = True)
# order
