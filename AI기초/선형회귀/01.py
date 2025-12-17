# 선형회귀








# 손실 함수
# 오차 측정
# 예측이 얼마나 틀렸는지 측정해야 함

# 오차 = 실제값 - 예측값 

# 문제 : 오차가 양수/음수 섞여 있으면 상쇄됨 
# 해결 : 오차를 제곱 ! 

# MSE ( Mean Squared Error)
# MSE = 평균((실제값 - 예측값) ^2 ) = 


import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np. array([2, 4, 5, 4, 5])

x_mean = np.mean(x)
y_mean = np.mean(y)

# 최소 제곱법
numerator = np.sum((x-x_mean) * (y-y_mean))
denominator = np.sum((x-x_mean)**2)

w = numerator / denominator
b = y_mean - w * x_mean

print(f"기울기 (w): {w :.4f}")
print(f"절편 (b): {b :.4f}")
print(f"예측식 (y): {w :.2f}x + {b:.2f}")

# Scikit - learn 으로 선형 회귀
from sklearn.linear_model import LinearRegression
x= np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# 모델 생성 및 학습
model = LinearRegression()
model.fit(x,y)

# 파라미터 확인
print(f"기울기 : {model.coef_[0]:.4f}")
print(f"절편 : {model.intercept_:.4f}")

# 예측
y_pred = model.predict(x)
print(f"예측값 : {y_pred}")




# 시각화
import matplotlib.pyplot as plt

# 폰트 깨짐 해결 
# plt.rcParams['font.family']

plt.figure(figsize=(10,6))

# 데이터 점
plt.scatter(x, y, color='blue', s=100, label='실제데이터')

# 회귀선
plt.plot(x, y_pred, color='red', linewidth=2, label='회귀선')

# 오차 시각화
for i in range(len(x)):
    plt.plot([x[i],x[i]], [y[i],y_pred[i]], 'g--', alpha=0.5 )


plt.xlabel('x')
plt.ylabel('y')
plt.title('선형 회귀')
plt.legend()
plt.grid(True)
plt.show()