# """ 구구단 만들기 """
# '''
# 목표 :
# 구구단 만들기
# 조건 :
# 함수의 이름은? GuGu
# 입력 받는 값은? 2
# 출력하는 값은? 2단(2, 4, 6, 8, ···, 18)
# 결과는 어떤 형태로 저장하지? 연속된 자료형이니까 리스트
# '''
#
# ''' 반복 많은 버전 '''
# def GuGu(n):
#     result = []
#     result.append(n * 1)
#     result.append(n * 2)
#     result.append(n * 3)
#     result.append(n * 4)
#     result.append(n * 5)
#     result.append(n * 6)
#     result.append(n * 7)
#     result.append(n * 8)
#     result.append(n * 9)
#     return result
# print(GuGu(2))
#
# ''' 축약 구상 '''
# i = 1
# while i < 10:
#     print(i)
#     i = i + 1
#
# ''' 구현 '''
# def GuGu(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i = i + 1
#     return result
# print(GuGu(2))

# """ 3과 5의 배수 합하기 """
# '''
# 목표 :
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9임  이들의 총합은 23임
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구함
# 조건 :
# 입력 받는 값은? 1부터 999까지(1000 미만의 자연수)
# 출력하는 값은? 3의 배수와 5의 배수의 총합
# 생각해 볼 것은? 하나. 3의 배수와 5의 배수는 어떻게 찾지?      둘. 3의 배수와 5의 배수가 겹칠 때는 어떻게 하지?
# '''
#
# ''' 1000 미만의 자연수 구하기 구상 '''
# #1
# n = 1
# while n < 1000:
#      print(n)
#      n += 1
# #2
# for n in range(1, 1000):
#      print(n)
# ''' 3과 5의 배수 구하기 '''
# # 3의 배수 구하기
# for n in range(1, 1000):
#      if n % 3 == 0:
#           print(n)
# # 3과 5의 배수 구하기
# result = 0
# for n in range(1, 1000):
#      if n % 3 == 0 or n % 5 == 0:
#          print(n)
#          result += n
# print(result)

# """ 게시판 페이징하기기 """
# '''
# 목표 : 총 건수와 페이지에 보여줄 게시물 수를 입력으로 주었을 때 총 페이지수를 출력하는 프로그램
# 게시물의 총 건수가 5이고 한 페이지에서 보여 줄 게시물 수가 10이면 총 페이지수는 1임
# 게시물의 총 건수가 15이고 한 페이지에서 보여 줄 게시물 수가 10라면 총 페이지수는 2가 될 것임
# ->> 5   10  1
#     15  10  2
#     25  10  3
#     30  10  3
#                 ->> 총 페이지수 = 총 건수 / 한 페이지당 보여줄 건수 + 1
# 조건 :
# 함수의 이름은? getTotalPage
# 입력 받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# 출력하는 값은? 총 페이지수
# '''
#
# ''' 기본 아이디어 함수로 만들기 '''
# def getTotalPage(m, n):
#      return m // n + 1
#
# print(getTotalPage(5,10))
# print(getTotalPage(15,10))
# print(getTotalPage(20,10))
# print(getTotalPage(25,10))
# print(getTotalPage(30,10))
#
# ''' 나머지 0일때 +1 안하기 '''
# def getTotalPage(m, n):
#     if m % n == 0:
#         return m // n
#     else:
#         return m // n + 1
#
# print(getTotalPage(5,10))
# print(getTotalPage(15,10))
# print(getTotalPage(20,10))
# print(getTotalPage(25,10))
# print(getTotalPage(30,10))

""" 메모장 만들기 """
'''
목표 : 메모장 만들기
조건 : 
필요한 기능은? 메모 추가하기, 메모 조회하기
입력 받는 값은? 메모의 내용, 프로그램 실행 옵션
출력하는 값은? memo.txt
python memo.py –a “Life is too short” -> 메모 추가
'''

''' -> memo1.py'''

''' 실행 '''
'''
C:\python>python memo.py –a “Life is too short” 
-a
Life is too short
----------------------
'''



""" 탭을 4새의 공백으로 바꾸기 """

'''
목표 : 문서 파일을 읽어서 그 문서 파일 내에 있는 탭(tab)을 공백(space) 4개로 바꾸어주는  스크립트
조건 : 
필요한 기능은? 문서 파일 읽어 들이기, 문자열 변경하기
입력 받는 값은? 탭을 포함한 문서 파일
출력하는 값은? 탭이 공백으로 수정된 문서 파일
python tabto4.py a.txt b.txt -> a의 'tab'을 b에서 'space'로
'''

''' 기본양식 (입력 출력) '''
''' -> tabto4 기본 양식으로 작성 -> 출력 테스트 -> 테스트 파일 작성 -> '''
'----------------------'



""" 하위 디렉터리 검색하기 """
'''
목표 : 특정 디렉터리부터 시작해서 그 하위의 모든 파일 중 파이썬(*.py)만 출력해 주는 프로그램 만들기

조건 : 

'''

''' 기본 뼈대 (경로 출력, 경로 검색) -> 디렉터리 경로 검색, 출력 -> 디렉터리 내 py파일 검색
    -> 하위까지 출력'''

