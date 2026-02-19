import requests
res = requests.get("http://www.naver.com", verify = False)

print(res.content)

parameters = {"code" : "005930"}
req = requests.get("https://finance.naver.com/item/sise.nhn", params = parameters, verify = False)
print(req.url)
print(res.text)

from bs4 import BeautifulSoup

html_txt = "<p class = 'weather' id = 'tw'>오늘의 날씨</p> <h1> 한때 소나기가 내리겠습니다. </h1>"

soup = BeautifulSoup(html_txt, "html.parser")

tag = soup.find("p")

print(tag)                  #tag 출력
print(tag.name)             #tag명 출력
print(tag.attrs)            #tag 속성 출력
print(tag.attrs["class"])   #tag 속성 중 class만 출력
print(tag.attrs["id"])      #tag 속성 중 id만 출력
print(tag.text)             #tag 내 텍스트 출력 