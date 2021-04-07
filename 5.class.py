'__adder__,__del_,__repr__ ....'
# #더하기
# result = 0
#
# def adder(num):
#     global result
#     result += num #_입력한 수 더함
#     return result #_출력
#
# print(adder(3))
# print(adder(4))

# #더하기2
#
# print("___________________")
# result1 = 0
# result2 = 0
# def adder1(num):
#     global result1
#     result1 += num
#     return result1
# def adder2(num):
#     global result2 #_전역변수이므로 누적됨됨    result2 += num
#     return result2
# print(adder1(3))
# print(adder1(4))
# print(adder2(3))
# print(adder2(7))

#더하기3
# class Calculator:
#      def __init__(self):    #_초기화. 객체 생성
#           self.result = 0   #_인수 없을때, 결과 0
#
#      def adder(self, num):  #_adder(인수 있을때)
#          self.result += num #_더하기
#          return self.result #_결과 출력
#
# cal1 = Calculator()
# cal2 = Calculator()
#
# print(cal1.adder(3))
# print(cal1.adder(4))
# print(cal2.adder(3))
# print(cal2.adder(7))

'개념 : a, navi : 객체. Simple(),Cat()의 인스턴스.'
# a = Simple()
# navi = Cat()
'개념 : self'
# class Service:
#     secret = "영구는 배꼽이 두 개다."
#     name = "안알랴쥼"
#     def setname(self, name):
#         self.name = name
#     def sum(self, a, b): # sum함수 써먹으려면 인스턴스까지(self) 인수 3개 넣어야함(파이썬의 특징)
#         result = a + b
#         print ("%s님 %s + %s = %s입니다." % (self.name, a, b, result))
#
# pey = Service()     # pey에 클래스 할당
# print(pey.secret)   # pey의 secret 인수
# pey.sum(3,5)        # pey의 sum 함수 (입력받는 인수 : pey, 3, 5)
# pey.setname("길똥이")
# pey.sum(3,5)
'예시 : __init__'
# babo = Service()
# babo.setname("바보") # 이 과정 필수로 하게 하려면? -> __init__
# babo.sum(1, 1)

# class Service:
#     secret = "영구는 배꼽이 두 개다."
#     def __init__(self, name):
#         self.name = name
#     def sum(self, a, b): # sum함수 써먹으려면 인스턴스까지(self) 인수 3개 넣어야함(파이썬의 특징)
#         result = a + b
#         print ("%s님 %s + %s = %s입니다." % (self.name, a, b, result))
#
# babo = Service('바부')
# babo.sum(1, 1)

'클래스 만들기'
'''사칙연산 만들자'''
# class FourCal:
#     def setdata(self, a, b):
#         self.a = a #선언된 인스턴트의 a는 a다
#         self.b = b
#     def sum(self):
#         c = self.a + self.b
#         return c
#     def sub(self):
#         c = self.a - self.b
#         return c
#     def mul(self):
#         c = self.a * self.b
#         return c
#     def div(self):
#         c = self.a / self.b
#         return c
#
# a = FourCal()   # 인스턴트 만들기
# a.setdata(4, 2) # 초기 설정
# print(a.sum())  # 함수
# print(a.sub())
# print(a.mul())
# print(a.div())

'''박씨네 집 만들기'''
class HousePark:
    def __init__(self, name, national):
        self.name = name
        self.national = national
    def lastname(self):
        if self.national == "한국" or self.national == "ko": #_한국이면 앞글자 자르기
            self.lastname = self.name[0:1]
            return self.lastname
        else:
            self.lastname = (self.name.split(' '))[1:2]     #_미국이면 공백기준으로 자르기
            return self.lastname
    def travle(self, where):
        print("%s, %s(으)로 여행을 감" % (self.name, where))
    def __add__(self, other):                               # 인스턴트 호출시 자동으로 더하기
        print("%s, %s 결혼했네" % (self.name, other.name))


pey = HousePark("박길동", "한국")
print(pey.name)
print(pey.lastname())
pey.travle('서울')

juliet = HousePark("조지 부시", "미국")
print(juliet.name)
print(juliet.lastname())
juliet.travle('타이페이')

class HouseKim(HousePark):
    def travle(self, where, day):
        self.name = "김" + self.name[1:]
        print("%s, %s(으)로 %d일 여행을 감" % (self.name, where, day))

pey = HouseKim("박길동", "한국")
print(pey.name)
print(pey.lastname())
pey.travle('서울', 10)

pey + juliet

