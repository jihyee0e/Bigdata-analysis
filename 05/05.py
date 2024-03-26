#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#1.test.csv 값을 읽어 dataframe 생성
df = pd.read_csv('test.csv')


# In[3]:


df


# In[4]:


#2.마지막 두 행만 출력하여 내용 확인
df.tail(2)


# In[5]:


#3.키가 180 이상인 행 출력
df[df['height']>=180]


# In[6]:


#4.키가 170 이상이고 성별이 여성인 행 출력
df[(df['height'] >= 170) & (df['sex'] == 'f')]


# In[7]:


#5.마지막 행에 ['anne',36,175,'f'] 새로운 데이터 삽입
df.loc[4] = ['anne',36,175,'f']
df


# In[8]:


#6.키가 170 이상이고 성별이 여성인 행에서 name과 age 열만 출력
df_col = df[(df['height']>=170) & (df['sex']=='f')]
df_col.loc[:, ['name', 'age']]

