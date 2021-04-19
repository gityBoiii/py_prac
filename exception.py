try:
     f = open('foo11.txt', 'r')
except FileNotFoundError as e1:
     print(str(e1))
else:
     data = f.read()
     f.close()


try:
     4 / 0
except ZeroDivisionError as e:
     print(e)

## (5_2_33)