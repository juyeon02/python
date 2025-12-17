# SDG : 확률적 경사 하강법
# Momentum : 이전 이동 방향의 관성을 반영해서 지역 최솟값을 넘어가게 해줌
# Adam : 학습률을 파라미터별로 적응적으로 조절


import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + 3 + np.random.randn(100) * 0.5 

# 파라미터 초기화 
w = 0.0
b = 0.0
lr = 0.1
epochs = 100

# 기록용
loss_history = []
w_history = []
b_history = []

# 경사 하강법 
for epoch in range(epochs):
    # 예측
    y_pred = w*x + b
    # 손실 계산 (MSE)
    loss = np.mean((y-y_pred) ** 2)
    loss_history.append(loss)

    # 그래디언트 계산
    dw = np.mean(2 * (y_pred - y) *x)
    db = np.mean(2 * (y_pred - y))

    # 파라미터 업데이트
    w = w - lr * dw
    b = b - lr * db

    # 기록
    w_history.append(w)
    b_history.append(b)

    if epoch % 20 == 0 : 
        print(f"Epoch {epoch:3d}: Loss = {loss:4f}, w = {w:.4f}, b = {b:.4f}")
print(f"최종: w = {w:.4f}, b = {b:.4f}")



import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 집값 데이터 생성
np.random.seed(42)
n_sample = 200

data = {
    '면적' : np.random.randint(15, 50, n_sample),
    '방수' : np.random.randint(1, 5, n_sample),
    '역거리' : np.random.randint(0.1, 2, n_sample),
    '층수' : np.random.randint(1, 25, n_sample),
    '건축년도' : np.random.randint(1990, 2023, n_sample)

}
 
집값 = (
    0.15 * data['면적'] + 
    0.5 * data['방수'] -
    0.3 * data['역거리'] + 
    0.02 * data['층수'] + 2 + 
    np.random.randn(n_sample) * 0.5 
 )

df = pd.DataFrame(data)
df['집값'] = 집값

print(df.head())
print(df.describe())