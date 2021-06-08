import sys
import urllib.request
import json
from bs4 import BeautifulSoup

parse = {'title': [], 'link': [], 'date': [], 'writer': []}
baseUrl = "https://www.silla.ac.kr"

# BeautifulSoup 객체생성
noticeUrl = ["/ko/index.php?pCode=anotice", "/ko/index.php?pCode=gnotice"]
print("0 학사공지 1 일반공지")
# param = int(input()) - 1
param = int(sys.argv[1])
if param == 0:
    print("학사공지 선택")
if param == 1:
    print("일반공지 선택")
selectBoard = param
dataJson = ['haksa.json', 'normal.json']

url = baseUrl + noticeUrl[selectBoard]
req = urllib.request.urlopen(url)
res = req.read()
soup = BeautifulSoup(res, 'html.parser')
bbs = soup.select_one("#contents > div.cont.div-conts > div.board-wrap > div.board-list-li-wrap")

# 파싱할 데이터
titleElements = bbs.select('ol > li > div > p > span > a > span')
linkElements = bbs.select('ol > li > div > p > span > a ')
writerElements = bbs.select('ol > li > div > p  span.writer ')
dataElements = bbs.select('ol > li > div > p > span.date')

# 지워야할 요소
removeList = []
# 파싱할 엘리먼트 텍스트만 가져오기
for date in dataElements:
    dateValue = date.get_text()
    parse['date'].append(dateValue)

for writer in writerElements:
    writerName = writer.get_text()
    parse['writer'].append(writerName)

for title in titleElements:
    titleName = title.get_text()
    parse['title'].append(titleName)

for link in linkElements:
    href = link.get('href')
    parse['link'].append(href)

# 지워야할 요소 검출
for i in range(len(parse['title'])):
    # print(i)
    if parse.get('title')[i] == '':
        removeList.append(i)

# 지워야할 요소 삭제
for removeindex in reversed(removeList):
    del parse.get('title')[removeindex]
    del parse.get('link')[removeindex]

# Convert Json

with open(dataJson[selectBoard], 'w') as outfile:
    json.dump(parse, outfile)
    print("파싱완료")