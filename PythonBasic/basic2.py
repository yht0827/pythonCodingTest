# 문자열 자료 형

# 문자열 개수 곱하기
a = "STRING"
print(a * 3)  # STRINGSTRINGSTRING

# 문자열 슬라이싱
a = "ABCDEF"
print(a[2:4])  # CD

# split 문자열 분리 빈 경우 공백 기준 으로 분리
data = "test/test2"
print(data.split("/"))  # ['test', 'test2']

data = "test test2"
print(data.split())  # ['test', 'test2']

# 앞 뒤 문자 중 인자에 들어가 있는 문자 제거
data = "test/"
print(data.strip('/'))  # test

# lstrip() 선행 문자 만 제거
data = "/test/"
print(data.lstrip('/'))  # test/

# rstrip() 후행 문자 만 제거
data = "/test/"
print(data.rstrip('/'))  # /test

# 첫 문자가 대문자
data = "abcde"
print(data.capitalize())  # Abcde

# 대 문자로 치환
data = "abcde"
print(data.upper())  # ABCDE

# 소 문자로 치환
data = "ABCDE"
print(data.lower())  # abcde

# count
ex_str = "following dialogue"
print(ex_str.count('o'))  # 3

print(ex_str.count('o', 0, 8))  # 2

# 입력한 인자로 시작 하는지 확인
ex_str = "https://www.naver.com"
print(ex_str.startswith('https'))  # True
print(ex_str.startswith('www', 8))  # True 8번째 인덱스부터 www

# 입력한 인자로 끝 나는지 확인
ex_str = "It’s been a long time!"
print(ex_str.endswith('time!'))  # True
print(ex_str.endswith('b', 3, 6))  # True

# find 가장 작은 인덱스를 돌려준다. 찾지 못하면 -1
ex_str = "https://www.naver.com"
print(ex_str.find("w"))  # 8
print(ex_str.find("C"))  # -1

# join : iterable 의 문자열들을 이어 붙인 문자열을 돌려준다.
data = [1, 2, 3, 4, 5]
print(*data)  # 1 2 3 4 5
print(" ".join(map(str, data)))  # 1 2 3 4 5

data = ['A', 'B', 'C', 'D', 'E']
print(*data)  # A B C D E
print(" ".join(data))  # A B C D E

# replace : 첫 번째 매개변수에 해당하는 값을 두 번째 값으로 모두 변경
data = "hihellohihello"
data = data.replace('hi', 'bye')  # byehellobyehello
print(data)

# replace 응용 - n개의 연속된 데이터를 1개로 압축
data = "helloooooooo"
while "oo" in data:
    data = data.replace("oo", "o")
print(data)  # hello

# 문자열 포맷팅 : f-string이 제일 빠르다.
name = 'Lena'
data = f'Hello {name}'
print(data)  # Hello Lena

fruit = 'apple'
price = 1000
data = f'The price of this {fruit} is {price + 100} won.'
print(data)  # 'The price of this apple is 1,100 won.'

domain = {'a': 'com'}
data1 = f'www.naver.{domain["a"]}'
print(data1)  # 'www.naver.com'
