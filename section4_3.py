import pandas as pd

score = pd.read_excel(r"C:\Users\JSS\python_excel\source\chapter04\성적 처리(수정).xlsx", sheet_name = "Sheet1")
score

# total_korean = score["국어"].sum(0)
# print(total_korean)

# score["sum"] = score.iloc[:, 2:7].sum(1)
# score["sum1"] = score["국어"] + score["영어"] + score["수학"] + score["사회"] + score["과학"]
# score.head()

# korean_avg = score["국어"].mean()
# print(korean_avg)

# score["평균"] = score.iloc[:, 2:7].mean(1)
# score["평균1"] = (score["국어"] + score["영어"] + score["수학"] + score["사회"] + score["과학"])/5
# # score.loc["과목평균"] = score.iloc[1:13,2:].mean(0)

# score1 = score[["반", "국어", "영어", "수학", "사회", "과학"]].groupby(["반"]).sum()
# # score2 = score.iloc[:, [0] + list(range(2,7))].groupby(["반"]).sum()
# score1
# # score2
# score2 = score[["반", "국어", "영어", "수학", "사회", "과학"]].groupby(["반"]).mean()
# score2 = round(score2, 1)
# score2

score["평균"] = score.iloc[:, 2:7].mean(1)
score["순위_오름"] = score["평균"].rank(ascending=True)
score["순위_내림"] = score["평균"].rank(ascending=False)
score["순위_내림_min"] = score["평균"].rank(method="min", ascending=False)
score.sort_values(by="평균", ascending=False)

score_row = score.iloc[:, list(range(2,7))]

score["MIN"] = score_row.min(1)
score["MAX"] = score_row.max(1)
score.describe()

