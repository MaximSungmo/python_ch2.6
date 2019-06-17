# textmode 가 default : t
f = open('test.txt', 'wt', encoding='utf-8')
# write함수는 writesize값을 리턴해준다.
writesize = f.write('안녕하세요.\n테스트 파일입니다.')
f.close()
print(writesize)

# binary mode : b
f = open('test2.txt', 'wb')
writesize = f.write(bytes('안녕하세요.\n테스트 파일입니다.', encoding='utf-8'))
f.close()
print(writesize)

# read test
f = open('test.txt', 'rt', encoding='utf-8')
# read함수의 return 값은 파일 내 들어있는 text이다.
text = f.read()
f.close()
print(text)

# binary read : copy
# 1단계 파일 읽기(정보 복사)
fsrc = open('python.jpg', 'rb')
data = fsrc.read()
fsrc.close()
print(type(data))
print(data)
# 2단계 파일 쓰기(붙여넣기)
fdest = open('python2.png', 'wb')
fdest.write(data)
fdest.close()

