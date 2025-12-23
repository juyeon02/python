# 손실함수

# 목적
# 모델 성능을 수치화
# 최적화 목표 제공
# 손실이 작을 수록 좋은 모델

# 다른 이름:
# 비용 함수 (cost Funtion)
# 목적 함수 (Objective Funtion)

import torch
import torch.nn as nn

# 예측과 실제
y_pred = torch.tensor([2.5, 0.0, 2.1, 7.8])
y_test = torch.tensor([3.0, -0.5, 2.0, 7.5])

# MSE 계산 (수동)
mse_manual = ((y_test - y_pred) ** 2).mean()
print(mse_manual)


# PyTorch MES 
mse_loss = nn.MSELoss()
mes = mse_loss(y_pred, y_test)
print(mes)

# MAE (Mean Absolute Error)

# 특징 
# 오차의 절대값 평균
# 이상치에 덜 민감 
# 0에서 미분 불가 

# 사용: 이상치가 있는 회귀 
mae_loss = nn.L1Loss()
mae = mae_loss(y_pred, y_test)
print(mae)

# Huber Loss 
# 특징 
# MSE 와 MAE 의 조합
# 작은 오차 : MSE처럼 동작
# 큰 오차 : MAE 처럼 동작

# 사용: 이상치가 일부 있는 경우 

huber_loss = nn.HuberLoss(delta=1.0)
huber = huber_loss(y_pred, y_test)
print(huber)

# BCE 분류 손실 함수
# 이진 분류용 
# 확률 예측 필요