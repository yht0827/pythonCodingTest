# 리스트 자료형

# 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 2차원 리스트 초기화 => 반드시 리스트 컴프리헨션을 이용해야 한다.
n = 3
m = 4
# n * m 2 차원 배열 초기화. array = [[0]*m] * n 은 문제가 됨 => 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식
array = [[0] * m for _ in range(n)]
print(array)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
array[1][1] = 5
print(array)  # [[0, 0, 0, 0], [0, 5, 0, 0], [0, 0, 0, 0]]

# 리스트의 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])  # 9 가장 마지막 원소
print(a[-3])  # 7

# 슬라이싱. 인덱스 1~3까지
print(a[1:4])  # [2, 3, 4]

# 리스트 컴프리핸션: iterable한 객체를 만드는 방법 list, tuple, dict에 대해서 가능
# 0 ~ 19까지 홀수만 담기
array = [i for i in range(20) if i % 2 == 1]
print(array)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 1 ~ 8까지 i * i 구하기
array = [i * i for i in range(1, 9)]
print(array)  # [1, 4, 9, 16, 25, 36, 49, 64]

# 리스트 정의
a = [1, 4, 3]
print(a)  # [1, 4, 3]

# append : 리스트 원소를 하나 삽입 / O(1)
a.append(2)
print(a)  # [1, 4, 3, 2]

# pop : 리스트 마지막 원소를 하나 제거 / O(1)
a.pop()
print(a)  # [1, 4, 3]

# 3. sort: 오름 차순 정렬 / O(nlog n)
a = [1, 4, 3, 2]
a.sort()
print(a)  # [1, 2, 3, 4]

# 4. sort(reverse=True): 내림 차순 정렬 / O(nlog n)
a.sort(reverse=True)
print(a)  # [4, 3, 2, 1]

# 5. reverse: 현재 원소의 순서를 모두 뒤집기 / O(n)
a.reverse()
print(a)  # [1, 2, 3, 4]

# 6. insert 2번 인덱스에 3를 넣기 / O(n)
a.insert(2, 3)
print(a)  # [1, 2, 3, 3, 4]

# 7. count: 해당 값 원소 개수 새기/ O(n)
print(a.count(3))  # [1, 2, 3, 3, 4] => 2

# 8.remove: 해당 값 원소 1개 제거 / O(n)
a.remove(3)
print(a)  # [1, 2, 3, 4]
