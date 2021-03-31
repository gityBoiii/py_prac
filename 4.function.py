# ## 함수
# def sum(a, b):
#     return a+b
#
# a=3;b=4
# c=sum(a,b)
# print("a + b = c :",c)
#
# def say():
#     return "hi"
#
# print(say())
#
# def sum(a,b):
#     d = print("%d + %d = %d"% (a,b,a+b))
#
# sum(3,6)
# print("d : ", d) ##결과값 반환 x

# #입력값 갯수 모를때
# def sum_many(*args): # "*" : 주소값 ㄴㄴ. 입력값들 튜플로
#     sum = 0
#     for i in args: # args 수 만큼
#         sum = sum + i
#     return sum
#
# result = sum_many(1, 2, 3)
# print(result)
#
# result = sum_many(1,2,3,4,5,6,7,8,9,10)
# print(result)

# # 변수마다 각각 다르게 계산
# def sum_mul(choice, *args):
#     if choice == "sum":
#         result = 0
#         for i in args:  # args 수 만큼
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
#
# result = sum_mul('sum', 1, 2, 3, 4, 5)
# print(result)
# result = sum_mul('mul', 1, 2, 3, 4, 5)
# print(result)

# # 결과값 2개
# def sum_and_mul(a,b):
#     return a+b, a*b
# print(sum_and_mul(3,4))
#
# def sum_and_mul2(a,b):
#     return a+b ## 여기서 빠져나감
#     return a*b
# print(sum_and_mul2(3,4))

# # 변수 여러개
# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("별명 : %s" % nick)
# say_nick('야')
#
# def say_myname(name, old, man=True):
#     print("이름 : %s" % name)
#     print("나이 : %d" % old)
#     if man:
#         print("남자")
#     else:
#         print("여자")
# say_myname('호호', 140, 0)

# ## 전역변수
# a = 1
# def vartest(a):
#     a = a + 1
#     return a
#
# a= vartest(3)
# print(a)
#
# b = 1
# def vartest_glob():
#     global b
#     b = b + 1
#
# vartest_glob()
# print(b)

# print(input("입력 : "))

for i in range(10):
    print(i, " ", end = '')