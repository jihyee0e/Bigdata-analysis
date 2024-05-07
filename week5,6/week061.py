from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import datetime

def hollys_store(result):  
    for page in range(1, 52): # p.173에 59로 잘못 표기(폐업으로 인한 매장 수 감소)
        hollys_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' % page
        #print(hollys_url)
        html = urllib.request.urlopen(hollys_url)  #url 접근
        soupHollys = bs(html, 'html.parser')  #해당 html 파싱
        tag_body = soupHollys.find('tbody')  #tbody 태그 찾기
    # print(tag_body)

        for store in tag_body.find_all('tr'):  #tbody.tr.td 태그 구하기
            store_td = store.find_all_next('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string

            result.append([store_name] + [store_sido] + [store_address] + [store_phone])


def main():
  result = []
  hollys_store(result)
  #pandas를 사용하여 테이블 형태의 데이터프레임 생성
  hollys_tbl = pd.DataFrame(result, columns=('store', 'sido_gu', 'address', 'phone'))
  #테이블 csv 파일로 저장
  hollys_tbl.to_csv('./hollys.csv', encoding='cp949', mode='w', index=True)
  print('------ 완료 ------')
  del result[:]

if __name__ == '__main__':
  main()