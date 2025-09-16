# 중요 메서드들
import copy
scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78
}

# setdeefault - 키가 없으면 추가, 있으면 기존 값 유지
scores.setdefault('정수진', 88)  # 새로 추가

# copy() - 얕은 복사
scores_copy = scores.copy()
scores_copy['최동훈'] = 95
print('scores', scores)
print('scores_copy', scores_copy)


# deepcopy() - 깊은 복사
deep = copy.deepcopy(scores)
nested_dict = {
    "team1": {'leader': '김철수', 'members': ['이영희', '박민수']},
    "team2": {'leader': '정수진', 'members': ['최동훈', '강미나']},
}

shallow = nested_dict.copy()  # 얕은 복사
deep = copy.deepcopy(nested_dict)  # 깊은 복사

# 원본값에 추가?
nested_dict['team1']['members'].append('신입')
print('shallow', shallow['team1']['members'])
print('deep: ', deep['team1']['members'])


# 순회
# scores = {
#    '김철수': 85,
#    '이영희': 92,
#    '박민수': 78
# }

# 키만 순회(기본)
for key in scores:
    print(f'{key}: {scores[key]}')

print()

for key in scores.keys():
    print(f'{key}: {scores[key]}')

print()

for value in scores.values():
    print(f'{value}')


# 평균 값 계산
average = sum(scores.values()) / len(scores)
print('average', average)

# 키 - 값 쌍 순회
for key, value in scores.items():
    print(f'{key}: {value}')


for idx, (key, value) in enumerate(scores.items(), 1):
    print(f'{idx}번째 {key} : {value}점')
