# 상속
'''
기존 클래스의 속성과 메서드를 물려받아 새로운 클래스를 만드는 것
동물 : 포유류 -> 개, 고양이(공통 특징: 자기, 먹기)
자동차 : 차량 -> 승용차, 트럭
가족: 부모 -> 자식 
'''

# 상속 없이 - 코드 중복 심각! ==> 상속으로 해결

'''
클래스 부모클래스
클래스 자식 클래스(부모클래스) ==> 부모클래스 상속

출력
dog1 = Dog('바둑이',3)
dog1.eat() # 바둑이가 먹습니다
'''


# 기본 문법과 용어
from abc import ABC, abstractmethod
class 부모클래스:
    # 부모 클래스 내용
    pass


class 자식클래스(부모클래스):  # 괄호 안에 부모클래스
    # 자식 클래스 내용
    pass

# 자식은 부모의 모든 것을 물려 받습니다.
# 부모의 모든 속성과 메서드를 자동으로 사용 가능
# 추가된 자신만의 속성과 메서드 정의 가능


class Person:  # 부모 클래스
    def __init__(self, Name, age):
        self.name = Name
        self.age = age

    def greet(self):
        print(f'안녕하세요, {self.name}입니다')


class Student(Person):
    def study(self):
        print(f'{self.name}이(가)공부합니다')


class Teacher(Person):
    def teach(self):
        print(f'{self.name}이 수업합니다')


student = Student('김학생', 20)
teacher = Teacher('박선생', 35)

# 부모 클래스 메서드 호출
student.greet()
teacher.greet()

# 자식 클래스 메서드 호출
student.study()
teacher.teach()


# super()와 생성자 상속
# super()
# super()는 자식 클래스에서 부모 클래스에 접근할 때 사용

# super()없이-문제발생
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'안녕하세요.{self.name}입니다')


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 부모 생성자 호출
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f'학생입니다. ')


student = Student('김철수', 20, '303003')
student.greet()


# 메서드 오버라이딩
# 오버라이딩
# 부모 클래스의 메서드를 자식 클래스에서 다시 정의 하는 것

class Animal:
    def make_sound(self):
        print(f"동물이 소리를 냅니다")


class Dog(Animal):
    def make_sound(self):
        print(f"멍멍")


class Cat(Animal):
    def make_sound(self):
        print(f"야옹")


animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        print(f'{self.name}의 넓이 {self.area}')


class Rectangle(Shape):
    def __init__(self, name):
        super().__init__(name)


# 추상 클래스
''' 
직접 객체를 만들 수 없고, 반드시 상속 받아서 완성해야 사용할 수 있는 미완성 설계도

동물 실제로 '동물'만 있는 건 없고, 개, 고양이, 새, 등 구체적인 동물이 있음

악기 - 추상적 개념 /  피아노, 기타, 드럼 - 구체적 개념
'''

# 추상 클래스는 왜 필요한가?
# 추상 클래스 없이


class Animal:
    def make_sound(self):
        pass  # 비어있음 - 구현을 까먹을 수 있음


class Dog(Animal):
    def eat(self):
        print('강아지가 밥을 먹습니다.')


dog = Dog()
dog.make_sound()  # 아무것도 안 일어남 - 버그!


# 추상 클래스 사용

class Animal(ABC):  # 추상 클래스!
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        pass

    def eat(self):
        print('강아지가 밥을 먹습니다')


dog = Dog()


# 기본 사용법
# from abc import ABC, abstractmethod
class 추상클래스이름(ABC):  # ABC 상속 필수
    @abstractmethod
    def 추상메서드이름(self):
        pass


class Animal(ABC):  # 추상 클래스!
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        pass

    def eat(self):
        print('강아지가 밥을 먹습니다')


animal = Animal()  # 추상 클래스는 직접 생성 불가
dog = Dog()  # 추상 메서드를 모두 구현했으므로 가능


class Shape(ABC):
    # 추상 클래스
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        # super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape = Shape
circle = Circle(5)
print(circle.area())


class Animal(ABC):  # 추상 클래스!
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 일반 메서드 _ 모든 동물이 공통으로 사용

    def sleep(self):
        print(f"{self.name}이가 잠을 잡니다 ")

    def eat(self):
        print(f"{self.name}이가 먹습니다")


# 추상 메서드 = 각 동물마다 다르게 구현해야 함


    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} 멍멍')

    def move(self):
        print(f'{self.name}이 가 뛰어다닙니다. ')


class Brid(Animal):
    def make_sound(self):
        print(f'{self.name} 짹짹')

    def move(self):
        print(f'{self.name}이 가 날아갑니다. ')


dog = Dog('바둑이', 3)
bird = Brid('참새', 1)

dog.eat()
bird.sleep()

dog.move()
bird.make_sound()
