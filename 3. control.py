# money = 1
# if money:
#     print("부릉부릉") ##들여쓰기 안하면 오류
# else:
#     print("뚜벅뚜벅")
#
# money = 2000
# card = 1
# if money >= 3000 or card:
#     print("부릉부릉")
# else:
#     print("뚜벅뚜벅")
#
# pocket = ['papaer', 'cellphone', 'money']
# if 'money' in pocket:
#     print("부릉부릉")
# else:
#     print("뚜벅뚜벅")
#
# pocket = ['papaer', 'cellphone']
# card = 1
# if 'money' in pocket:
#     print("부릉부릉")
# else:
#     if card:
#         print("부릉부릉")
#     else:
#         print("뚜벅뚜벅")
#
# pocket = ['papaer', 'cellphone', 'money']
# if 'money' in pocket:pass
# else:
#     print("카드")
#
# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무 %d번 찍음" % treeHit)
#     if treeHit == 10:
#         print("나무 주그음")
#
# number = 1
# while number < 5:
#     number = int(input("숫자 입력 : "))
#     if number == 1:
#         print("add")
#     if number == 2:
#         print("del")
#     if number == 3:
#         print("list")
#     if number == 4:
#         print("quit")
#
#
# coffee = 10
# money = 300
# while money:
#     print("커피 퉤")
#     coffee = coffee - 1
#     print("남은 커피 : %d" % coffee)
#     if not coffee:
#         print("커피 없음")
#         break

# coffee = 10
# while True:
#     money = int(input("돈 넣어"))
#     if money == 300:
#         print("커피 퉤")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름돈 : %d, 커피 퉤" % (money-300))
#         coffee = coffee - 1
#     else:
#         print("돈 퉤, 커피 x")
#         print("남은 양 : %d" % coffee)
#     if not coffee:
#         print("커피 없음. 안 팜")
#         break

## 선증가 후처리
# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0:continue
#     print(a)

# ##for문 구조에서, list 불러오기
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# ##두개씩 부르기 가능
# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first, last)

# marks = [50, 60, 40, 90, 87]
# number = 0
# for mark in marks:
#     number = number +1
#     if mark < 60: continue ## 60이 안되면 처음부터
#     print("%d번째 당첨" % number)
#
# # 범위
# a = range(10)
# print("a: ", a)
#
# sum = 0
# for i in range(1, 11):
#     sum = sum + i
# print("sum : ", sum)

# marks = [50, 60, 40, 90, 87]
# for number in range(len(marks)): ## 리스트 갯수만큼 돌리기
#     if marks[number] < 60: continue
#     print("%d번째 합격" % (number+1))
#
# for i in range(2,10): ## 행
#     for j in range(1,10): ## 렬
#         print(i*j, end=" ") ## 붙여서 출력
#     print("") ## 줄바꿈

## list 안에 for 문
# a = [1,2,3,4]
# result = []
# for num in a: ## num 선언
#     result.append(num*3)
# print(result)

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

### 구구단
a = [1,2,3,4]
result = [x*y for x in range(2,10)
                for y in range(1,10)]
print(result)