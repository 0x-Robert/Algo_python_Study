#클래스 예제
import math

"""
hypot 쓰인 함수 설명
math.hypot(*coordinates)
유클리드 크기(norm) sqrt(sum(x**2 for x in coordinates))를 반환합니다. 원점에서 coordinates로 지정된 점까지의 벡터의 길이입니다.

2차원 점 (x, y)의 경우, 피타고라스 정리를 사용하여 직각 삼각형의 빗변(hypotenuse)을 계산하는 것과 동등합니다, sqrt(x*x + y*y).

버전 3.8에서 변경: n 차원 점에 대한 지원이 추가되었습니다. 이전에는, 2차원인 경우만 지원되었습니다.

math.hypot(x, y)	가로 x 세로 y인 직각삼각형의 빗면의 유클리드 거리를 반환합니다.	root(x^2 + y^2)
x*x + y*y에서 루트씌웠다고 생각하면 됨
"""
#주클래스 점
#서브클래스 원은 점클래스를 상속받는다.
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x #데이터 속성(attribute)
        self.y = y
    def distance_From_origin(self): #메서드 속성
        return math.hypot(self.x,self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "point ({0.x!r}, {0.y!r}".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r}".format(self)


class Circle(Point):
    def __init__(self,radius,x=0, y=0):
        super().__init__(x,y) #생성 및 초기화
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_From_origin()- self.radius)

    def area(self):
        return math.pi*(self.radius**2)

    def circumference(self):
        return 2*math.pi*self.radius

    def __eq__(self,other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return "circle ({0.radius!r}, {0.x!r})".format(self)

    def __str__(self):
        return repr(self)
        