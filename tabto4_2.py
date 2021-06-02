import sys
src = sys.argv[1]
dst = sys.argv[2]

f = open(src) ## 입력 파일 열기 
tab_content = f.read() ## 읽기
f.close() ## 닫기

space_content = tab_content.replace("\t", " "*4) ## 탭 -> 공백 4개로 변환
print(space_content) ## 출력
