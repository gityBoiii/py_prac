# ## 리스트
# # 자료형
# odd = [1, 3, 5, 7, 9]
# a = []
# b = [1, 2, 3]
# c = ['Life', 'is', 'too', 'short']
# d = [1, 2, 'Life', 'is']
# e = [1, 2, ['Life', 'is']]
#
# print(odd, '\n',
#       a, '\n',
#       b, '\n',
#       c, '\n',
#       d, '\n',
#       e)
#
# # 인덱스
# #_ 1차
# a = [1, 2, 3]
# print('a :', format(a))
# print('a : %s' %(a))
# print('a[0] :', a[0])
# print('a[-1] : %s' %(a[-1]))
# a = [1, 2, 3, ['ㄱ', 'ㄴ', 'ㄷ']]
# print('a[3] : %s' %(a[3]))
# #_ 2, 3차
# print('a[-1][0] : %s' %(a[-1][0]))
# print('a[3][1] : %s' %(a[3][1]))
# a = [1, 2, 3, ['ㄱ', 'ㄴ', ['aa', 'bb']]]
# print('a[3][2]) : %s' %(a[3][2]))
# print('a[3][2][1]) : %s' %(a[3][2][1]))
#
# # 슬라이싱
# a = [1, 2, 3, 4, 5]
# print('a[1:4] : %s' %(a[1:4]))
# print('a[:2] : %s' %(a[:2]))
# print('a[2:] : %s' %(a[2:]))
# a = [1, 2, 3, ['ㄱ', 'ㄴ', ['aa', 'bb']]]
# print('a[2:4] : %s' %(a[2:4]))
#
# #연산자
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# print(a*2 + b)
# # print(a[2] + 'hi') ## 같은 자료형이 아니라 오류
# a[2] = 4
# print(a)
# print(a[1:2])
# b = []
# a[1] = ['ㄱ', 'ㄴ', 'ㄷ']
# b = b + a
# print('b :', b)
# print(a)
# a[1] = []
# b[1:2] = []
# print(a)
# print(b)

# # 함수
# #_ append, sort, reverse, index, insert, remove, pop, count, extend
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.append(0)
# print(a)
# a.append([5, 6])
# print(a)
# a = [4, 5, 1, 7, 2, 3]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# print(a.index(7))
# a = [1, 2, 3]
# a.insert(0, 4)
# print(a)

# # 게임
# import random
# myList = ['하나', '둘', '셋', '넷', '다섯', '여섯']
#
# while(True):
#     response = input('주사위 계속? (yes, no)');
#     if response == 'yes' or response == 'y':
#         coin = random.choice(myList)
#         print(coin)
#     else:
#         break

# # 튜플 ##수정 불가
# t1 = ()
# t2 = (1,)
# t3 = (1,2,3)
# t4 = 1,2,3
# print(t1, t2, t3, t4)
# #_ 인덱싱, 연산자는 됨
# print(t3[2])

# # 딕셔너리 ##키:뜻
# dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print('dic :', dic)
# print({'first':'hi'})
# print({'first':['hi','bye','hey']})
# a = {'first':'hi'}
# a['second'] = 'yoooo'
# print(a)
# a['first'] = 'kiyaaa'
# print(a)
# del(a['first'])
# print(a)
# print(a['second'])
# a = {'second':'hi', 'second':'heyyyyy'} ##하나만 출력
# print(a)
# a = {'second':'hi', 'third':'haha', 'fourth':'yoooo'}
# print(a.keys()) ##dict_keys 객체 -> list()로 변환
# print(a.values())
# print(a.items())
# a.clear()
# print(a)
# a = {'second':'hi', 'third':'haha', 'fourth':'yoooo'}
# print(a.get('second'))
# print(a['second'])
# print(a.get('third', 'new val')) ##있으면 가져오고 없으면 2번째 출력
# print(a)
# flag = 'name' in a
# print(flag)
# flag = 'haha' in a
# print(flag)
# flag = 'third' in a
# print(flag)
# ##_사전 작성
# eng_dict =dict()
#
# eng_dict['one'] = '하나'
# eng_dict['two'] = '둘'
# eng_dict['three'] = '셋'
# eng_dict['four'] = '넷'
# eng_dict['five'] = '다섯'
# eng_dict['six'] = '여섯'
# eng_dict['seven'] = '일곱'
# eng_dict['eight'] = '여덟'
#
# word = input('단어 입력 :')
# print(eng_dict.get(word, '없음'))

# # 집합 자료형 ##중복x, 순서x -> 인덱싱 x
# s1 = set([1,2,3])
# print(s1)
# s2 = set('hello')
# print(s2)
# l1 = list(s1) ##변환해서 인덱싱
# print(l1)
# print(l1[0])
# t1 = tuple(s1)
# print('t1 :',t1)
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# print('s1 & s2 :', s1 & s2)
# print('s1.intersection(s2) :', s1.intersection(s2))
# print('s1 | s2 :', s1 | s2)
# print('s1.union(s2) :', s1.union(s2))
# print('s1 - s2 :', s1 - s2)
# print('s2 - s1 :', s2 - s1)
# print('s1.difference(s2) :', s1.difference(s2))
# s1 = set([1,2,3])
# s1.add(4)
# print(s1)
# s1.update([5,6,7])
# print(s1)
# s1.remove(5)
# print(s1)
# #참 : 문자열, 1, 숫자,... ||| 거짓 : 공백, 0
# a = [1,2,3,4]
# while a:
#     print("a는 : ", a.pop())

# 자료형 대입
a = 1
b = "python"
c = [1,2,3]

print("a:", a,
      "\nb:", b,
      "\nc:", c)

a = 3
b = 3
c = a is b

print("a:", a,
      "\nb:", b,
      "\nc:", c)

# ##함수 불러오기
# import sys
# print("getrefcount:",sys.getrefcount(3)) ##참조 번수
#
# a, b = ("python", "life")
# print("a, b:", a,b)
# a = b
# print("a = b -> a:",a)
#
# ## 값 서로 뒤바꾸기
# a = 3
# b = 5
# a, b = b,a
# print("a : ", a)
# print("b : ", b)
#
# a = [1,2,3]
# b = a
# a[1] = 4
# print("a:", a)
#
# a = [1,2,3]
# b = a[:] ## ':'=전체
# a[1] = 4
# print("a:", a)
# print("b:", b)


