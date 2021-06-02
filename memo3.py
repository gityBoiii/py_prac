import sys

option = sys.argv[1]

if option == '-a':
     memo = sys.argv[2]
     f = open('c:\python\\bigdata_programing\\memo.txt', 'a')
     f.write(memo)
     f.write('\n')
     f.close()
elif option == '-v':
     f = open('c:\python\\bigdata_programing\\memo.txt')
     memo = f.read()
     f.close()
     print(memo)
