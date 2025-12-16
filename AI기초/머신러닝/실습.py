# 와인 데이터셋으로 분류 모델 만들기 
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# 0. 데이터 로드
wine = load_wine()
X, y = wine.data, wine.target

# 1. 훈련 / 테스트 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print(f"훈련: {X_train.shape} 테스트: {X_test.shape}") 

# 2. 스케일러 생성 및 학습
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. 모델 비교 _  딕셔너리로 관리 
models = {
    'Logistic': LogisticRegression(max_iter=10000),
    'Dec': DecisionTreeClassifier(),
    'random': RandomForestClassifier(),
    'SVC' : SVC(),
    'KNN' : KNeighborsClassifier()
}

print("스케일링 전")
for name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{name}: {score:.2%}")

print("스케일링 후")
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    score = model.score(X_test_scaled, y_test)
    print(f"{name}: {score:.2%}")

# 4. 가장 좋은 모델 선택 
best_model = RandomForestClassifier()
best_model.fit(X_train_scaled, y_train)
best_score = best_model.score(X_test_scaled, y_test)

print("최종 선택 모델 : 랜덤포레스트 ")
print(f"최종 정확도: {best_score:.2%}")

