import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# 광고비(백만원)와 매출(천만원) 데이터
광고비 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
매출 = np.array([3, 5, 6, 8, 11, 13, 14, 16, 17, 20])

# 1. 선형 회귀 모델 학습

# 모델 생성 및 학습 
model = LinearRegression()
model.fit(광고비, 매출)

# 2. 기울기와 절편 확인
w = model.coef_[0]
b = model.intercept_

print(f"기울기 : {model.coef_[0]:.4f}")
print(f"절편 : {model.intercept_:.4f}")
print(f"예측식 : {model.coef_[0]:.4f}x광고비 + {model.intercept_:.4f}")

y_pred = model.predict(광고비)
print(f"예측값 : {y_pred}")

# 3. 광고비 15백만원일 때 매출 예측
ad_15 = np.array([[15]])
pred_15 = model.predict(ad_15)

print(f"광고비 15백만원 예상 매출: {pred_15}천만원")

# 4. R2 Score 계산
y_pred = model.predict(광고비)
r2 = r2_score(매출, y_pred)

print(f"R² Score: {r2:.4f}")



# 실습

import pandas as pd
from sklearn.datasets import fetch_california_housing
# 데이터를 훈령용/ 테스트용으로 나누기 위한 함수
from sklearn.model_selection import train_test_split
# 평균 0, 표준편차 1로 맞추는 표준화(스케일링) 도구
from sklearn.preprocessing import StandardScaler 
# 다중 선형 회귀 모델
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



# 1. 데이터 준비
housing = fetch_california_housing()

x = housing.data
y = housing.target
# 각 열의 이름 
feature_names = housing.feature_names

# 2. 데이터 확인
df = pd.DataFrame(x, columns=feature_names)
df['Target'] = y

print('데이터 크기:',x.shape)
# 평균, 표준편차, 최솟값, 최댓값 확인 
print(df.describe())

# 3. 학습/테스트 분할
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size= 0.2,  # 20% 테스트
    random_state= 42 # 결과 재현용
)


# X. 스케일링
scaler = StandardScaler()  # 스케일러 객체 생성
# train 기준으로 훈련 데이터로 평균, 표준편차 학습 및 변환
x_train_scaled = scaler.fit_transform(x_train) 
# 훈련 데이터 기준으로 테스트 데이터만 변환 
x_test_scaled = scaler.transform(x_test)

# 4. 다중 선형 회귀 모델 학습
model = LinearRegression() # 선형 회귀 모델 생성
# 내부적으로 각 특성의 가중치(계수) 계산
model.fit(x_train_scaled, y_train)

# 5. R² Score 확인
y_pred = model.predict(x_test_scaled) # 테스트 데이터로 집값 예측
r2 = r2_score(y_test, y_pred)

print(f"R2 score : {r2:.4f}")

# 6. 각 특성의 중요도 분석

coef_df = pd.DataFrame({
    '특성': feature_names,
    '계수': model.coef_
}).sort_values(by='계수', ascending=False)

print("\n특성 중요도 :")
print(coef_df)