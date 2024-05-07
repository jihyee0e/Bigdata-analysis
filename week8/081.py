import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt

##1-1 데이터 준비1
#엑셀에서 열 구분자 세미콜론으로 인식시키기
red_df = pd.read_csv('./wine+quality/winequality-red.csv', 
                            sep=';', header=0, engine='python')
red_df.to_csv('./winequality-red2.csv', 
                     index=False)

#엑셀에서 열 구분자 세미콜론으로 인식시키기

white_df = pd.read_csv('./wine+quality/winequality-white.csv', 
                              sep=';', header=0, engine='python')
white_df.to_csv('./winequality-white2.csv', 
                       index=False)

##1-2.데이터 준비2
#데이터 병합하기
red_df.head()  #red_df 5번째까지 출력
red_df.shape  #행과 열 개수 출력
red_df.insert(0, column='type', value='red')  #와인 종류 구분하는 type 열 추가
red_df.head()
red_df.shape

white_df.head()  #white_df 5번째까지 출력
white_df.shape  #행과 열 개수 출력
#와인 종류 구분하는 type 열 추가
white_df.insert(0, column='type', value='white')  #열 0번째에 type-red,white 구분 변수 추가
white_df.head()
white_df.shape

wine = pd.concat([red_df, white_df])
wine.to_csv('./wine.csv', index=False)
wine.shape

##2. 데이터 탐색
#기본 정보 확인 - info(): DataFrame을 구성하는 행/열 크기, 컬럼 이름, 값의 자료형 등 출력
#print(wine.info())

#띄어쓰기가 되어있으면 인식 어려우니까 _으로 바꿔주기
wine.columns = wine.columns.str.replace(' ', '_') 
desResult = wine.describe()  #기술 통계값 출력
#print(desResult)
desResult.to_csv('./descriptive.csv')

sorted(wine.quality.unique())  #wine의 컬럼 quality의 유일한 값만 오름차순으로 출력 
#print(sorted(wine.quality.unique()))  #>>[3, 4, 5, 6, 7, 8, 9]
wine.quality.value_counts()  #속성값 빈도수 출력
#print(wine.quality.value_counts())

##3.데이터 모델링: 기술 통계 분석
# wine.groupby('type')['quality'].describe()  #type별 quality 열 기술 통계값
# wine.groupby('type')['quality'].mean()  #type별 quality 열 평균값

#다중 통계량 구하기
# wine.groupby('type').agg(['mean','var'])  #type으로 그릅화하고 column마다 평균, 분산 출력
# wine.groupby('type').agg({'quality':'mean', 'alcohol':'max'})  #type으로 그룹화하고 quality의 평균값, alcohol의 최대값 출력
# type의 그룹화하고 quality, alcohol의 평균, 표준편차
# wine.groupby('type').agg({'quality':['mean', 'std'], 'alcohol':['mean','std']})

##4. 데이터 모델링: 회귀 분석
#다중회귀분석: '종속변수~독립변수1+..+독립변수n'
#종속변수(y), 독립변수(x1~x10): type, quality 제외 11개 속성
Rformula = 'quality~fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'  

regression_result = ols(Rformula, data=wine).fit()
regression_result.summary()  #요약
# print(regression_result.summary())  #요약

##5. 회귀 분석 모델로 새로운 샘플 품질 등급 예측
#wine에서 종속변수를 제외하고 독립변수만 추출하여 저장
sample1 = wine[wine.columns.difference(['quality','type'])]
sample1 = sample1[0:5][:]  #0~4번까지 5개, 열은 처음~끝까지 다시 저장
#print(sample1)

#샘플 데이터를 회귀분석모델 regression_result 예측 함수에 적용하여 예측값 저장
sample1_predict = regression_result.predict(sample1)  #예측 함수 적용하여 예측하기
sample1_predict  #quality 확인하기
wine[0:5].quality  #0~4번까지 샘플 quality 값 출력하여 맞게 예측된건지 확인

#회귀식에 사용한 독립변수에 대입할 임의의 값을 딕셔너리 형태로 만들기
data={"fixed_acidity":[8.5,8.1], "volatile_acidity":[0.8,0.5], "citric_acid":[0.3,0.4], 
      "residual_sugar":[6.1,5.8], "chlorides":[0.055,0.04], "free_sulfur_dioxide":[30.0,30.1],
      "total_sulfur_dioxide":[98.0,99], "density":[0.996,0.91], "pH":[3.25,3.01], 
      "sulphates":[0.4,0.35], "alcohol":[9.0,0.88]}
sample2 = pd.DataFrame(data, columns=sample1.columns)  #sample1의 열 이름만 뽑음
#print(sample1.columns)  #quality, type을 제외한 11개의 열(=독립변수)
sample2_predict = regression_result.predict(sample2)  #예측 함수 적용하여 예측하기
sample2_predict
#print(sample2_predict)  #quality 확인하기

##6. 와인 유형에 따른 품질 등급 히스토그램 그리기
#커널 밀도 추정 적용한 히스토그램 그리기
sns.set_style('dark')
#차트에서 x축은 quality, y축은 확률 밀도 함수값
sns.histplot(red_df['quality'], kde=True, color='red', label='red wine')
sns.histplot(white_df['quality'], kde=True, label='white wine')
plt.title('Quality of Wine Type')  #그래프 제목
plt.legend()
plt.show()  #시각화

##7. 부분 회귀 플롯으로 시각화하기
fig = plt.figure(figsize=(8,13))  #차트 크기 지정
#다중 선형 회귀 분석 결과를 가지고 있는 regression_result를 이용하여 각 독립변수의 플롯 구하기
sm.graphics.plot_partregress_grid(regression_result, fig=fig)
plt.show()  #시각화