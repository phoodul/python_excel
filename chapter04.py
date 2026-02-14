import pandas as pd
data = {"이름" : ["홍길동", "이순신", "강감찬", "임꺽정", "이성계"],
        "출생년도" : [1980, 1986, 1990, 1985, 1988],
        "점수" : [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)

df = df.rename({"출생년도": "출생"}, axis = "columns")
df[["이름", "출생"]]
df[1:3]
print(df.loc[1:2, ["이름", "출생"]])

df #df 출력
df["보너스"] = df["점수"] * 5
df
df["지역"] = ["서울", "서울", "부산", "대구", "인천"]
df

del df["보너스"]
df
df.loc[5] = ["김순신", 1980, 3.3, "광주"]
df

df.iloc[4, 1] = 1999
df.drop(5, inplace=True)
df