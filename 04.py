#!/usr/bin/env python
# coding: utf-8

# ### Test04. numpy 실습
# - 세 반의 평균, 최고점, 최저점 출력

# In[1]:


import numpy as np

#1.세 반 정의
class1 = [89, 54, 101, 39, 92]
class2 = [77, 92, 100, 107, 82]
class3 = [120, 68, 91, 49, 48]

#2.100점이 초과된 점수는 100점으로 처리
for i in range(5):
    if class1[i] > 100:
        class1[i] = 100
        
    if class2[i] > 100:
        class2[i] = 100
        
    if class3[i] > 100:
        class3[i] = 100
    
#3.세 반을 모두 합친 새로운 배열 생성
sum_class = np.stack((class1, class2, class3))

print(sum_class)
#4.평균, 최고점, 최저점 출력
print("전체 평균: ", np.mean(sum_class))  #평균 출력
print("최고점: ", np.max(sum_class))  #최고점 출력
print("최저점: ", np.min(sum_class))  #최저점 출력


# In[ ]:


#class_sum = [[89, 54, 101, 39, 92], 
#             [77, 92, 100, 107, 82],
#             [120, 68, 91, 49, 48]]

#for i in range(3):
#    for j in range(5):
#        if class_sum[i][j] > 100:  #2.100점이 초과된 점수는
#            class_sum[i][j] = 100  #100점으로 처리

