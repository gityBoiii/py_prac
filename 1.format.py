# ## 숫자형
# # 정수형
# a = 123
# a1 = -178
# a2 = 0
# print (a, a1, a2)
# # 실수형
# a3 = 1.2
# a4 = -3.45
# print (a3, a4)
# # 지수
# a5 = 4.2E10
# a6 = 4.2e10
# print(a5, a6)
# # 8진수 16진수
# a7 = 0o177 #ox
# a8 = 0x5ff #hex
# b = 0xABC
# print(a7, a8, b)
# # 복소수
# a = 1 + 2j #i대신 j
# b = 3 - 4J
# print(a, b)
# a = 1 + 2j
# print(a, a.real)
# a = 1 + 2j
# print(a.imag) #imaginary
# # 사칙연산
# a = 3
# b = 4
# print(a + b, a * b, a / b, a ** b)
# print(7 % 3, 3 % 7) #나머지
# print(7/4, 7//4) #몪만

## 자료형
# 문자형
s = "Hello World"
s2 = "Hello World"
s3 = """Hello World"""
s4 = "'Hello World'"
s5 = '"Hello World"'
s6 = """Hello World
hihihi
heyheyhey"""
print(s)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s + s6)
print(s * 2)
print(s * 100) #여러번 반복 가능
print(s[0], s[1], s[2], s[2], s[-4], s[-2], s[-1]) #배열
print(s[0:5])
s = "Hello World"
print(s * 100) #여러번 반복 가능
print(s[0], s[1], s[2], s[2], s[-4], s[-2], s[-1]) #배열
print(s[:5] + '!' + s[6:])
print(s[0:5]) #슬라이싱
print(s[5:])
print(s[:])
print(s[5:-2]) #빼기
print(s[:5])
print(s[5:])
print(s.count('W'))
print(s.find('W'))
print(s)
s2 = ','
print(s.join('TEST'))
s3 = s2.join('TEST')
print(s3)
print(s3.split(',')) #나누기
print("{0} day".format(3))      #포맷
print("{0} day".format("five"))
a = 10
print("{0} day".format(a))
print("{0:<10}".format("!!!")) #자릿수, 정렬 맞추고 format으로 삽입
print("{0:>10}".format("!!!"))
print("{0:^10}".format("!!!"))
print("{0:=^10}".format("!!!")) #자릿수 채우고 정렬 맞추고 format으로 삽입

# 입력
a = int(input("숫자 입력해"))
b = int(input("숫자 입력해"))
print("숫자", a, ",", b, " : a + b = ", a+b )
print("숫자 %d, %d : a + b = %d" % (a,b,a+b))
print("숫자 %d, %d : a + b = %10d" % (a,b,a+b))
print("숫자 %d, %d : a / b = %f" % (a,b,a/b))
print("숫자 %d, %d : a / b = %0.4f" % (a,b,a/b))


