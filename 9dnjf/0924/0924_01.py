# 파일 입출력
'''
파일 입출력(file I/O)은 프로그램이 파일을 읽고(input) 쓰는 (output) 작업입니다. 
프로그램이 종료되어도 데이터를 보관할 수 있는 유일한 방법.
프로그램의 데이터는 메모리에 저장되는데 프로그램이 종료되면 메모리의 데이터는 사라집니다. 
파일로 저장하면 하드디스크에 영구 보관됩니다. 
'''

# 파일 입출력이 필요한 상황ㅇㅇㅇㅇ
'''
1. 설정 파일 저장 : 게임 설정, 프로그램 옵션
2. 데이터 백업:  중요한 정보 보관
3. 로그 기록: 프로그램 실행 기록, 에러 추적
4. 데이터 교환: 엑셀, csv 파일로 다른 프로그램과 데이터 공유
5. 대용량 처리: 메모리에 다 못 담는 빅데이터 처리
'''

# 위험한 방법  - 파일을 안 닫을 수 있기 때문에
# 1단계 : 파일 열기(open) - 파일과 연결 통로 생성
file = open('data.txt', 'r', encoding='utf-8')

# 2단계 : 파일 작업(Read/Write) - 데이터 읽기/ 쓰기
content = file.read()
print(content)

# 3단계 : 파일 닫기 (close) - 연결 종료
file.close()


# 안전한 방법 2 - with문(권장!)

with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# with 사용시 자동으로 close됨

# 새 파일 생성 또는 덮어쓰기
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World! \n')
    f.write('파이썬 파일 입출력')

# 1. read() - 파일 전체를 하나의 문자열로
# 메모리 비효율적 전체 사용
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# read(크기) - 저장한 크기만큼만
# 메모리 효율적 = 한 줄씩 처리
with open('data.txt', 'r', encoding='utf-8') as f:
    print(f'처음 위치: , {f.tell()}')  # 일반적으로 0
    content = f.read(3)
    print(f'3바이트 읽은 후  위치: , {f.tell()}')  # 9
    print(content)

# 2. readline() - 한 줄씩 읽기
with open('data.txt', 'r', encoding='utf-8') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1.strip())  # strip() : 공백, 탭(\t), 줄바꿈 제거
    print(line2.strip())
    f.seek(0)
    line3 = f.realline()
    print(line3.strip())

# readline() - for문
print('2. readline()-for문')
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:   # 한 줄씩만 메모리에 사용
        print(line.strip())

# 3. readlines()
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # [첫줄\ㅜ. \둘째줄\n

    for line in lines:
        print(line.strip())
