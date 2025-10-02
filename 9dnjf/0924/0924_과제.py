'''
# 실습1. 회원 명부 작성하기
with open('member.txt', 'w', encoding='utf-8') as f:
    for i in range(3):
        name = input(f'{i + 1}번 회원: 이름을 작성하세요: ')
        pw = input(f'{i + 1}번 회원: 비밀번호를 입력하세요: ')
        f.write(f'{name} {pw} \n')

with open('member.txt', 'r', encoding='utf-8') as f:
    for data in f:
        print(data.strip())


# 실습2. 회원 명부를 이용한 로그인 기능
name_user = input(f'이름을 입력하세요: ')
pw_user = input(f'비밀번호를 입력하세요: ')

with open('member.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, pw = line.strip().split()
        if name == name_user and pw == pw_user:
            print('로그인 성공')
            break
        else:
            print('로그인 실패')


# 실습3. 로그인 성공 시 전화번호 저장하기

name_user = input(f'이름을 입력하세요: ')
pw_user = input(f'비밀번호를 입력하세요: ')

with open('member.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, pw = line.strip().split()
        if name == name_user and pw == pw_user:
            print('로그인 성공')
            number = input('전화번호 입력(000-0000-0000): ')

            members = {}  # dict 생성
            with open('member.txt', 'a', encoding='utf-8') as f2:
                for line in f2:
                    saved_name, saved_phone = line.strip().split()
                    # key - value 값 지정 _ 딕셔너리에 추가
                    members[saved_name] = saved_phone
            # 딕셔너리에 추가, 있으면 수정
            members[name_user] = number

            with open('member.txt', 'a', encoding='utf-8') as f2:
                for name, phone in members.items():

            break

        else:
            print('로그인 실패')


# 3. 새로운 사람이 로그인 성공 시 member_tel.txt에 전화번호 추가하기
# 4. member_tel.txt에 이미 존재하는 사람이 로그인 성공 시 전화번호 수정하기





login_success = False
with open("member.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, pw = line.strip().split()
        if input_name == name and input_pw == pw:
            login_success = True
            break

if login_success:
    print("로그인 성공")
    phone = input("전화번호를 입력하세요: ")

    # 기존 데이터 읽기
    tel_data = {}
    try:
        with open("member_tel.txt", "r", encoding="utf-8") as f:
            for line in f:
                n, p = line.strip().split()
                tel_data[n] = p
    except FileNotFoundError:
        pass

    # 전화번호 추가/수정
    tel_data[input_name] = phone

    # 다시 저장
    with open("member_tel.txt", "w", encoding="utf-8") as f:
        for n, p in tel_data.items():
            f.write(f"{n} {p}\n")

    print("전화번호가 저장되었습니다.")
else:
    print("로그인 실패")'''

'''
# 문제 1: 나이 입력 프로그램
연령대를 출력하는 프로그램을 작성하세요.

• 음수나 150 초과는 오류 메시지
• 정상 입력 시 연령대 출력(미성년자/청년/중년/노년)

'''

'''
def get_age_group():
    try:
        age = int(input("나이를 입력해주세요: "))

        if age < 0 or age > 150:   # 범위 벗어나면 오류 메시지
            print("나이는 0 이상 150 이하만 입력할 수 있습니다.")
        elif age < 19:
            print("미성년자")
        elif 20 <= age <= 30:
            print("청년")
        elif 31 <= age <= 50:
            print("중년")
        else:
            print("노년")

    except ValueError:   # 숫자가 아닌 입력 처리
        print("숫자만 입력해 주세요.")


get_age_group()
'''

# 리스트의 특정 인덱스 값을 안전하게 가져오는 함수를 작성


def safe_get(lst, index, default=None):
    """
    리스트에서 안전하게 값 가져오기
    - lst: 리스트
    - index: 인덱스
    - default: 기본값
    """
    # 여기에 코드 작성
    try:
        return lst[index]

    except IndexError:
        return default


# 테스트
numbers = [10, 20, 30]
print(safe_get(numbers, 1))      # 20
print(safe_get(numbers, 10))     # None
print(safe_get(numbers, 10, -1))  # -1
