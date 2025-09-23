# 모듈
'''
모듈
파이썬 코드가 저장된 파일 입니다. 
함수, 변수, 클래스 등을 모아놓은 파일로 다른 프로그램에서 가져다 쓸 수 있습니다. 

도구상자: 여러 도구(함수)를 모아둔 상자(모듈)
레고 블록: 필요한 블록(모듈)을 가져와서 조립
요리 레시피: 필요한 레시피(모듈)을 참고해서 요리
'''

# 모듈이 필요한 이유
'''
1. 코드 재사용: 한 번 작성한 코드를 여러 곳에서 사용
2. 유지보수: 기능별로 분리하여 관리가 쉬움
3. 협업: 팀원들과 코드 공유가 편리
4. 네임스페이스: 이름 충돌 방지
'''

# 전체 모듈 가져오기 (ctrl+ 클릭)
'''import calculator
result = calculator.add(10, 5)
print(result)'''


# 작성되어있는 모듈


'''import math as m # 별칭
import random
import datetime

print(m.pi)  # 별칭 사용
print(random. randint(1, 10))
print(datetime.datetime.now())



import calc
result = calc.add(10, 5)
print(result)

result = calc.div(10, 0)
print(result)

'''

# 패키지
'''
패키지(package)는 모듈들을 모아 놓은 디렉토리
관련된 모듈들을 체계쩍으로 관리할 수 있습니다. 

'''

from mypackage.module_2 import hello
from mypackage.module_1 import greet
from mypackage import module_1
from mypackage import module_2

module_1.greet()
module_2.hello()


# 가상환경?
# 프로젝트별로 독립적인 패키지 환경을 만들 수 있습니다
# python -m venv myenv(이름) : 가상환경 생성
# source myenv/Scripts/activate : 활성화 코드
# deactivate : 비활성화 코드

# pip
# 파이썬 패키지 관리자
