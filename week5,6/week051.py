import os, sys
import urllib.request
import datetime, time
import json

client_id = 'KKGokoFlbXLeh4SLGnFD'
client_secret = 'iWfWqaM6X8'

### [CODE 1] ###
def getRequestUrl(url):  
  req = urllib.request.Request(url)  #접속 요청 객체
  req.add_header("X-Naver-Client-Id", client_id)
  req.add_header("X-Naver-Client-Secret", client_secret)

  try:
    response = urllib.request.urlopen(req)  #서버에서 받은 응답을 저장하는 객체
    if response.getcode() == 200:  #요청 정상 처리
      print("[%s] Url Request Success" % datetime.datetime.now())
      return response.read().decode('utf-8')  #utf-8 형식으로 디코딩하여 반환
  except Exception as e:  #예외사항 발생 시
    print(e)
    print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))  #에러 메시지 출력
    return None


### [CODE 2] ### : 네이버 뉴스를 반환하고, json 형식으로 변환
def getNaverSearch(node, srcText, start, display):
  base = "https://openapi.naver.com/v1/search"
  node = "/%s.json" % node  #네이버 검색 API를 이용하여 검색할 대상 노드
  parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

  url = base + node + parameters
  responseDecode = getRequestUrl(url)  # [CODE 1]

  if (responseDecode == None):
    return None
  else:
    return json.loads(responseDecode)  #서버에서 받은 JSON 형태의 응답 객체를 파이썬 객체로 로드하여 변환


### [CODE 3] ### : json 데이터를 리스트 타입으로 변환
def getPostData(post, jsonResult, cnt):
  #post 객체 __ 항목에 저장된 값
  title = post['title']
  description = post['description']
  org_link = post['originallink']
  link = post['link']

  #문자열을 날짜 객체 형식으로 변환
  pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
  pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')  #날짜 객체의 표시 형식 지정

  #리스트 객체인 jsonResult에 원소 추가
  jsonResult.append({'cnt': cnt, 'title': title, 'description': description,
                     'org_link': org_link, 'link': org_link, 'pDate': pDate})
  return


### [CODE 0] ###
def main():
  node = 'news'  # 크롤링 할 대상
  srcText = input('검색어를 입력하세요: ')  #검색어 입력받아서 srcText에 저장
  cnt = 0
  jsonResult = []

  #함수를 호출하여 start=1, display=100에 대한 검색 결과를 반환받아 jsonResponse에 저장
  jsonResponse = getNaverSearch(node, srcText, 1, 100)  # [CODE 2]
  total = jsonResponse['total']

  while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
    for post in jsonResponse['items']:
      cnt += 1
      getPostData(post, jsonResult, cnt)  # [CODE 3]

    #getNaverSearch() 함수를 호출하여 새로운 검색 결과를 저장하고 for문 다시 반복
    start = jsonResponse['start'] + jsonResponse['display']
    jsonResponse = getNaverSearch(node, srcText, start, 100)  # [CODE 2]
  print('전체 검색 : %d 건' % total)

  with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf-8') as outfile:
    jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(jsonFile)

  print("가져온 데이터 : %d 건" % (cnt))
  print('%s_naver_%s.json SAVED' % (srcText, node))



if __name__ == '__main__':
  main()