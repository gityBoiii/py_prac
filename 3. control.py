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
coffee = 10
money = 300
while money:
    print("커피 퉤")
    coffee = coffee - 1
    print("남은 커피 : %d" % coffee)
    if not coffee:
        print("커피 없음")
        break

