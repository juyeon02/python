# from sklearn.어디서든 import 모델

# 1. 모델 생성
# model = 모델(하이퍼파라미터)

# 2. 학습
# model.fit(x_train, y_traiin)

# 3. 예측
# predictions = model.predict(x_test)

# 4. 평가 
# score = model.score(x_test, y_test)

from sklearn.datasets import load_iris

iris = load_iris()
print(f"특성: ", iris.feature_names)
print(f"타겟:" , iris.target_names)

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split


x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size = 0.2,
    stratify = y,
    random_state = 42

)


print(f"훈련: {x_train.shape} 테스트: {x_test.shape}")


from sklearn.neighbors import KNeighborsClassifier
# 1. 모델생성 (k)

model = KNeighborsClassifier(n_neighbors=3)

# 2. 학습
model.fit(x_train, y_train)

# 3. 예측
y_pred= model.predict(x_test)
print("예측결과: ",y_pred [:10])
print("실제결과: ", y_test[:10])

# 4. 모델 평가
from sklearn.metrics import accuracy_score, classification_report

# 4. 정확도 
accracy = accuracy_score(y_test, y_pred)
print(f"정확도: {accracy: .2%}")

# 간단히 
print(f"정확도: {model.score(x_test, y_test): .2%}")

# 상세 리포트
print(classification_report(y_test, y_pred, target_names=iris.target_names))


# 로지스틱
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)
print(f"로지스틱 회귀 정확도: {model.score(x_test, y_test): .2%}")


# 결정트리
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
print(f"결정트리 회귀 정확도: {model.score(x_test, y_test): .2%}")

# 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(x_train, y_train)
print(f"랜덤포레스트 회귀 정확도: {model.score(x_test, y_test): .2%}")


# 딕셔너리로 관리 방법
models = {
    'Logistic': LogisticRegression(),
    'Dec': DecisionTreeClassifier(),
    'random': RandomForestClassifier()
}

for name, model in models.items():
    model.fit(x_train, y_train)
    print(f" {name} 정확도: {model.score(x_test, y_test): .2%}")



# 데이터 전처리
# 스케일링의 중요성
# 특성별 스케일이 다르면 문제!
print("원본 데이터 범위: ")
print(f"특성1: {x[:,0].min():.1f} ~ {x[: , 0]. max():.1f}")
print(f"특성2: {x[:,1].min():.1f} ~ {x[: , 1]. max():.1f}")

# 범위가 다르면 일부 특성이 과도한 영향 
from sklearn.preprocessing import StandardScaler

# 스케일러 생성 및 학습
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

print('스케일링 후')
print(f"평균:  {x_train_scaled.mean(axis=0)}")
print(f"표준편차:  {x_train_scaled.std(axis=0)}")

from sklearn.svm import SVC

# 스케일링 없이 
model = SVC()
model.fit(x_train, y_train)
print(f"스케일링 전: {model.score(x_test, y_test):.2%}")

# 스케일링 후 
model = SVC()
model.fit(x_train_scaled, y_train)
print(f"스케일링 후: {model.score(x_test_scaled,y_test ): .2%}")