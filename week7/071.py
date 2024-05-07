from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time

#[CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    #AttributeError: 'str' object has no attribute 'capabilities'
    #>>selenium은 크롬드라이브를 따로 다운받지 않아도 사용할 수 있는 기능을 제공하고 있기 때문에 
    #'./chromedriver'를 하면 오류가 발생한다. -> './chromedriver' 제거하여 바로 사용하기
    driver = webdriver.Chrome()
    #driver.implicitly_wait(3)  #웹 페이지 연결할 동안 3초 대기

    id=0  #csv 파일 만들 때, 필요한 id 값

    for i in range(1, 50):  #매장 수 만큼 반복
        driver.get(CoffeeBean_URL)  #커피빈 매장 페이지를 여는 작업
        try:  #실패 예외처리
            driver.execute_script("storePop2(%d)" %i)  
            time.sleep(1)  #스크립트 실행 할 동안 1초 대기
            html = driver.page_source

            soupCB = BeautifulSoup(html, 'html.parser')

            # with open('soupCBHhtml.txt', 'w', 'encoding=utf8') as outfile:
            #     outfile.write(soupCB.prettify())

            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            print(i, store_name)  #출력창에 매장 이름 출력하기

            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2]) 
            store_address = store_address_list[0]  #매장 주소
            store_phone = store_info[3].string  #매장 전화번호
            id=id+1
            result.append([store_name] + [store_address] + [store_phone])
        except:
            print(i, 'fail')
            continue

    #driver.quit()
    return

#[CODE 0]
def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)  #[CODE 1]

    CB_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding='cp949', mode='w', index=True)

if __name__ == '__main__':
    main()