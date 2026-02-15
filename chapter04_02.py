import pandas as pd

info = pd.read_excel(r"C:\Users\JSS\python_excel\source\chapter04\직원 정보.xlsx", sheet_name = "Sheet1")
info
info = pd.read_excel(r"C:\Users\JSS\python_excel\source\chapter04\직원 정보.xlsx", sheet_name = "Sheet1")
info["성명"] = info["성"] + info["이름"]
info["성명1"] = info[["성", "이름"]].sum(1)
info["사원번호 앞 4자리"] = info["사원번호"].str[0:4]
info["전화번호 뒤 4자리"] = info["전화번호"].str[9:13]
info["구"] = info["주소"].str.split(" ").str[1]
info[["성", "이름", "전화번호", "구"]]

info["대문자"] = info["영문명"].str.upper()
info["첫 글자"] = info["영문명"].str.capitalize()

info[["순번", "성", "이름", "영문명", "전화번호", "대문자", "첫 글자"]]
info["phone"] = info["전화번호"].str.replace("-", "", 1)
info["phone1"] = info["전화번호"].str.replace("-", " ")
info[["순번", "성", "이름", "전화번호", "phone", "phone1"]]
