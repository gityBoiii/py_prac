"""내장 함수"""

''' 수학 '''
# # 절대값
# print(abs(-3));
# print("----------")
# # pow ( 제곱 )
# print(pow(2, 4))
# print("----------")
# # all (AND 연산)
# print(all([1,2,3]));
# print(all([1,2,0]));
# print("----------")
# # any (OR 연산)
# print(any([1,2,3]));
# print(any([1,2,0]));
# print(any([0,0,0]));
# print("----------")
# # chr (아스키 문자로)
# print(chr(97))
# print("----------")
# # ord (아스키코드)
# print(ord('a'))
# print(ord('0'))
# # int (정수로)
# print(int('555'))
# print(int('111', 2)) ## 2진법으로
# print(int('12', 16)) ## 16진법으로
# print("----------")

# str (문자열로)
print(str(333))
print(str('hi'))
print(str('hi'.upper()))

# # eval (evaluation, 문자열 자동 변환 -> 계산)
# print(eval('1+2'))
# print(eval('divmod(7,3)'))
# print("----------")
# # filter (걸러줌)
# def positive(numberList):
#      result = []
#      for num in numberList:
#           if num > 0:
#                result.append(num)
#      return result
#
# print(positive([1, -3, 2, 0, -5, 6]))
# print("-----")
# def positive(x):
#     return x > 0
#
# print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# print("----------")
# # hex (hexadecimal. 16진법으로)
# print(hex(234))
# print("----------")
# # divmod (몫, 나머지)
# print(divmod(5, 2))
# print("----------")
# # enumerate (인덱스와 같이 리턴)
# for i, name in enumerate(['body', 'foo', 'bar']):
#     print(i, name)
# a = ['hong','gil','dong']
# b = list(enumerate(a))
# c = dict(enumerate(a))
# print(b)
# print(c)
# print("----------")


''' 입력 '''
# # input (입력)
# a = input("입력하셈 : ")
# print (a)

''' 주소, 함수 '''
# # id (주소값)
# a = 3
# print(id(3))
# print(id(3))
# print(id(4))
# print("----------")

# isinstance (인스턴트인지 판별)
class Person: pass ## Person 클래스 생성
a = Person()
print(isinstance(a, Person)) ## Person의 인스턴스?

b = 3
print(isinstance(b, Person))
print("----------")

# lambda ( Λ λ. def 없이 함수 만들기 )
plusTen = lambda a: a+10
print(plusTen(3))
print("-----")

sum = lambda a, b: a+b ## << 변수 여러 개일시 괄호 쳐야 함
print(sum(3,4))
print("-----")

myList = [lambda a, b:a+b, lambda a, b:a*b]
print(myList[0](5,6))
print(myList[1](5,6))
print("----------")

''' 리스트 '''
# len (리스트 길이)
print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))
print("----------")

# list (리스트로 반환)
print(list("python"))
print(list((1,2,3)))
print("----------")

# map (1 대 1 대응)
def two_times(numberList):
     result = []
     for number in numberList:
          result.append(number*2)
     return result

result = two_times([1, 2, 3, 4])
print(result)
print("-----")
def two_times(x): return x*2
list(map(two_times, [1, 2, 3, 4]))
print(result)
print("-----")
def plus_one(x):
    return x + 1
print(list([1, 2, 3, 4, 5]))
print(list(map(plus_one, [1, 2, 3, 4, 5])))
print("----------")

# max (리스트 최대값 리턴)
print(max([1,2,3]))
print(max("python"))
print("----------")
# min (리스트 최대값 리턴)
print(min([1,2,3]))
print(min("python"))
print("----------")
# range (범위 지정)
print(list(range(5)))
print(list(range(5, 10)))
print("----------")
print(list(range(5, 10, 2)))
print(list(range(5, 10, -1)))
print(list(range(5, -5, -1)))
# sorted (정렬)
print(sorted([3,1,2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))

''' 파일 '''
# 파일 열기
# f = open("새파일.txt", "r")
# fb = open("새파일.txt", "rb")
# print(f)
# print(f.name)
# print(f.read())
# print(fb)
# print(fb.name)
# print(fb.read())





