#!/usr/bin/env python
# coding: utf-8

# ### Test03. 사용자 정의 함수
# - 로또 번호 뽑기

# In[13]:


import numpy as np
import pandas as pd

#B.lottoFunc() 함수를 통해 뽑은 로또 번호를 저장하는 list 정의
lotto_list = []
print("로또 추첨을 시작합니다.")

#A.lottoFunc() 함수 구현
def lottoFunc():
     while 1:  #중복 발생되면 되돌아가기
        if len(lotto_list) >= 6:
            break
            
        #A.추첨된 로또 번호(1-45) 하나를 반환
        number = np.random.randint(1,46)
        
        #새로 뽑은 번호가 list에 없으면, 
        if number not in lotto_list:
            lotto_list.append(number)  #리스트에 추가
        lotto_list.sort()
                
lottoFunc()
print("이번 번호 ---> ", format(lotto_list))

