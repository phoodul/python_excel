#matplotlib : 다양한 형태의 그래프 함수 및 서식 편집 기능 제공
#pandas: 데이터 프레임 내 데이터를 요약, 전처리 후 그래프를 그릴 수 있는 함수 제공
#seaborn: 색상 테마와 통계 등을 추가하여 그래프를 그릴 수 있는 기능 제공

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"

'''
pyplot은 파이썬의 대표적인 시각화 라이브러리인 Matplotlib의 모듈 중 하나입니다.

역할: 복잡한 그래프를 아주 쉽게 그릴 수 있도록 도와주는 인터페이스 역할을 합니다.

특징: 상태 기반(state-based)으로 작동합니다. 즉, "그림판을 만들고, 선을 긋고, 제목을 붙여라"라는 명령을 내리면 내부적으로 현재 활성화된 그림판을 찾아 차례대로 적용해 줍니다.

rcParams는 Runtime Configuration Parameters의 약자
설정 항목,설명,예시 코드
font.size,글자 크기 조절,plt.rcParams['font.size'] = 12
figure.figsize,"그래프의 기본 크기(가로, 세로)","plt.rcParams['figure.figsize'] = (10, 6)"
axes.unicode_minus,마이너스 기호 깨짐 방지,plt.rcParams['axes.unicode_minus'] = False
lines.linewidth,선의 굵기,plt.rcParams['lines.linewidth'] = 2
'''

'''
plot: 선 그래프
scatter: 산점도
bar: 수직 막대 그래프
barh: 수평 막대 그래프
pie: 원 그래프
hist: 히스토그램
boxplot: 상자 수염 그래프
'''

'''
그래프 옵션
xlim, ylim: x축, y축 범위: plt.xlim(-1, 1)
grid: 격자 눈금: plt.grid(True) # 격자 생성
legend:  범례 위치 지정            : plt.legend(2)
        1: 우측 위, 2: 좌측 위
        3: 좌측 아래, 4: 우측 아래
        6: 좌측 중앙, 7: 우측 중앙
        8: 하측 중앙, 9: 상측 중앙 
xlabel, ylabel: x축, y축 타이틀   : plt.xlabel("시간")
title: 그래프 제목 : plt.title("월간매출") # 그래프 제목을 "월간매출"로 설정
xticks, yticks: x축, y축 눈금 조정
'''

'''
선 그래프
plt(x, y, color, lw) # x = x축 데이터, y = y축 데이터, color = 색상, lw = 선 두께
plt.plot([1, 10], [1,1], linestyle = "solid")
linestyle "dashed" : 파선 "dashdot" : 쇄선 "dotted": 점선 
'''

# 선 그래프 그리기

height = [155, 160, 163, 167, 170, 174, 178, 182, 186, 190]
weight = [44, 46, 48, 50, 57, 62, 70, 74, 79, 82]
plt.title("선 그래프")
plt.xlabel("몸무게")
plt.ylabel("키")
plt.plot(weight, height, color = "red", lw =3)
plt.show()

height = [155, 160, 163, 167, 170, 174, 178, 182, 186, 190]
weight = [44, 46, 48, 50, 57, 62, 70, 74, 79, 82]
plt.title("스캐터 플랏")
plt.xlabel("몸무게")
plt.ylabel("키")
plt.scatter(weight, height)
plt.show()