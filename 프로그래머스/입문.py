array = [1, 2, 3, 3, 3, 4]

num = []   # 이미 센 숫자 저장
for i in array:
    if i not in num:         # 처음 보는 숫자일 때만 출력
        count = array.count(i)
        num.append(i)        # 센 숫자 기록
        print(max(num))


array = [1, 2, 3, 3, 3, 4, 4, 4]

max_count = 0     # 최빈값 등장 횟수
mode = None       # 최빈값 숫자

for num in array:
    count = array.count(num)   # num이 몇 번 나오는지 세기
    if count > max_count:      # 지금까지 최고값보다 크면
        max_count = count      # 최고값 갱신
        mode = num             # 최빈값 숫자 갱신

print("최빈값 숫자:", mode)


if num not in checked:           # 처음 보는 숫자만
    count = array.count(num)
     checked.append(num)

      print(num)

       if count > max_count:       # 더 큰 개수 나오면
            max_count = count
            mode_list = [num]       # 최빈값 리스트 갱신

        elif count == max_count:    # 같은 개수 나오면
            mode_list.append(num)   # 최빈값 리스트에 추가

    # 2️⃣ 최빈값이 하나인지 여러 개인지 확인
if len(mode_list) == 1:
    print(mode_list[0])            # 하나면 숫자 반환
else:
    print(-1)                     # 여러 개면 -1 반환



array = [1, 2, 3, 3, 3, 4, 4]

# 먼저 최대 등장 횟수 찾기
max_count = 0
for num in array:
    count = array.count(num)
    if count > max_count:
        max_count = count

# 2️⃣ 최빈값들 찾기
mode = []
for num in array:
    if array.count(num) == max_count and num not in mode:
        mode.append(num)

# 3️⃣ 최빈값 반환
if len(mode) == 1:
    print(mode)
else:
    print(-1)


array = [1, 2, 3, 3, 3, 4, 4]

stack = []

for i in array:
    nums = array.append.count(i)
    print(nums)
    if array.count(i) == i not in nums:
        stack.append(i)
        print(stack)



array = [1, 2, 3, 3, 3, 4, 4]

# 이미 센 숫자를 기록할 리스트
num = []

for i in array:
    if i not in num:           # 처음 보는 숫자만 세기
        count = array.count(i)     # num이 몇 번 나오는지 세기
        num.append(i)          # 이미 센 숫자 기록

        
        print(i, ":", count)          # 숫자와 개수 출력 
