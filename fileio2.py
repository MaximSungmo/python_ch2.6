
# test.txt 파일을 read, 'utf-8'로
f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
# 두 번 읽으면 file pointer가 맨 끝에 있으므로 공백을 읽게 됨
text = f.read()
print('------', text)

# file pointer를 움직이는 방법
# 1. open 함수를 받은 f 변수에서 tell(binary read의 poisition)을 확인한다.
# 즉, tell함수를 이용한 리턴 값은 byte
pos = f.tell()
print(pos)

# seek() 함수를 이용해서 file pointer 위치에서 (f.tell()) byte만큼 앞 쪽으로 이동
# f.seek(offset, from_what)
# f.seek(n, 0) 처음 위치를 0으로 시작해서 text mode에서는 0(파일 시작)만 허용
# f.seek(n, 1) 현재 위치를 기준으로
# f.seek(n, 2) 맨 마지막을 기준으로
print('맨 첫 위치')
f.seek(16)
# print('맨 마지막 위치')
f.seek(0, 2)
text = f.read()
print(text)

# seek 함수 적용을 위해 binary mode
f = open('123.txt', 'wb')
f.write(b'0123456789')
f.close()

f = open('123.txt', 'rb')
print(f.tell())

f.seek(5, 1)
data = f.read(2)
print(data)

f.seek(0, 2) # file pointer 맨 끝으로 이동
f.seek(-5, 1)
data = f.read(3)
print(data)

# line 단위로 읽기
linenum = 0
f2 = open('fileio.py', 'rt', encoding='utf-8')
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break
    linenum += 1
    # print('{0}:{1}'.format(linenum, line), end='')

# readlines()함수를 사용한 방법
f3 = open('fileio.py', 'rt', encoding='utf-8')
lines = f3.readlines()
# print(lines)
f3.close()

for linenum, line in enumerate(lines):
    # print('{0}:{1}'.format(linenum, line), end='')
    print('')


# with ~ as 구문을 활용한 자동 자원 정리
# f3 = open()
with open('fileio2.py', 'r', encoding='utf-8') as f4:
    for linenum, line in enumerate(f4.readlines()):
        print('{0}: {1}'.format(linenum, line), end='')
print(f4.closed)

