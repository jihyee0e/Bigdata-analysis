#!/usr/bin/env python
# coding: utf-8

# ## Test02. 점심메뉴 정하기

# In[1]:


import numpy as np
import pandas as pd


# In[35]:


#A.food list
food = ['pizza', 'poke', 'kimchijjigae', 'yogurt', 'gimbap', 'pasta', 'hamburger']
#print(len(food))

#1.메뉴 하나 추천하기
recom_num = np.random.randint(len(food))

print(food)
print("오늘 추천 점심 메뉴는 바로 --->", food[recom_num])

#2.메뉴 정렬하기
sort_food = sorted(food)
print()
print(sort_food)

#3.리스트에 추가할 메뉴가 있는지 질문
order = input("추가하고 싶은 메뉴가 있나요? ")

for i in range(1000):
    if order == 'y':  #3-a.리스트에 추가할 메뉴가 있다면
        #메뉴 입력 받기
        addmenu = input('add menu(if you stop) q): ')
        sort_food.append(addmenu)
        if addmenu == 'q':  #3-b.그만 입력받으려면 'q' 입력받아 무한루프 종료
            sort_food.remove('q')
            break
        elif order == 'n':  #3-c.없으면 4번으로 바로 이동
            sort_food.remove('n')
            print(sort_food)  #4.추가된 메뉴 포함해서 출력
            break
            
#5."찾고 싶은 음식은" 질문 출력 후, 메뉴 입력 받기
print(sort_food)
find_food = input("What food do you want to find? ")

if find_food not in sort_food:   #만약 리스트에 있는 음식이 아니라면
    print(find_food, "is not in list")
else:  #찾고싶은 음식과 리스트에 있는 음식이 같다면
    #6.해당 메뉴가 몇 번째 있는지 출력
    #index가 0부터 시작이니 +1을 해주어 1~부터 시작하게 출력
    print(sort_food.index(find_food) + 1, "' in the list")

