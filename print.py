## 기본 출력을 위한 print 함수
import sys

print(1)
print('hello', 'world')

# sep 파라미터
x = 0.2
s = "hello"
print(x)
print(s)

# 기본적으로 ',' 로 구분이 되면 separator가 ' '로 동작한다
print(x, s, sep=' ')
print(x, s)

# 기본적인 print() 함수 호출
print('abc', 'des', sep=' ', end='\n')

# file 파라미터를 지정
print('Hello World', file=sys.stdout)
print('Error: Hello World', file=sys.stderr)

# file 출력
# hello.txt를 write모드로 연 후 file=f에 Hello World를 작성한다.
f = open('hello.txt', 'w')
print(type(f))
print('Hello World', file=f)
f.close()

# 참고
sys.stdout.write('Hello World!!!!!!!!!!!!!')