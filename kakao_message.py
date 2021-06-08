import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
dataJson = ['haksa.json', 'normal.json']
templateHader = ['학사 공지', '일반 공지']
with open(dataJson[0]) as f:
    result = json.load(f)
Token = ''
# 사용자 토큰
template_id = 54909
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer '+Token,
}

template_args = {
    'header': templateHader[0],

    'title1': result.get('title')[0],
    'date1': result.get('date')[0],
    'writer1': result.get('writer')[0],
    'link1': result.get('link')[0],

    'title2': result.get('title')[1],
    'date2': result.get('date')[1],
    'writer2': result.get('writer')[1],
    'link2': result.get('link')[1],

    'title3': result.get('title')[2],
    'date3': result.get('date')[2],
    'writer3': result.get('writer')[2],
    'link3': result.get('link')[2],

    'title4': result.get('title')[3],
    'date4': result.get('date')[3],
    'writer4': result.get('writer')[3],
    'link4': result.get('link')[3],

    'title5': result.get('title')[4],
    'date5': result.get('date')[4],
    'writer5': result.get('writer')[4],
    'link5': result.get('link')[4],
}
dict1 = {
    'template_args': json.dumps(template_args)
}
res = requests.post('https://kapi.kakao.com/v2/api/talk/memo/send?template_id=54909', headers=headers,
                    data=dict1)

if res.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))
