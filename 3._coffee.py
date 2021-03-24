coffee = 10
while True:
    money = int(input("돈 넣어"))
    if money == 300:
        print("커피 퉤")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 : %d, 커피 퉤" % (money-300))
        coffee = coffee - 1
    else:
        print("돈 퉤, 커피 x")
        print("남은 양 : %d" % coffee)
    if not coffee:
        print("커피 없음. 안 팜")
        break