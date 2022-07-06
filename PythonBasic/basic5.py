# 스택 => 리스트 자료형을 이용하여 스택으로 사용 pop(), append()를 이용

# 큐
from collections import deque

# deque 정의
# dq = deque()
dq = deque([1, 2, 3, 4, 5])
print(dq)  # 1 2 3 4 5

# deque 리스트에 추가
# 맨 뒤에 추가
dq.append(6)
print(dq)  # 1 2 3 4 5 6
# 맨 앞에 추가
dq.appendleft(0)
print(dq)  # 0 1 2 3 4 5 6

# deque 리스트에서 제거
# 맨 뒤에서 제거
dq.pop()
print(dq)  # 0 1 2 3 4 5

# 맨 앞에서 제거
dq.popleft()
print(dq)  # 1 2 3 4 5

# rotate: x 값 만큼 회전 해준다.음수면 왼쪽, 양수면 오른쪽으로 회전한다. 기본값은 1
dq.rotate()
print(dq)  # 5 1 2 3 4
dq.rotate(-2)
print(dq)  # 2 3 4 5 1

# 힙
# 최댓값/최솟값을 O(1)에 찾을 수 있는 자료구조
# 기본적으로 heapq는 최소 힙으로 구성
import heapq

# 최소 힙
_list = [32, 16, 54, 94, 81, 31]

# heapify: 리스트를 힙 자료구조로 변환
heapq.heapify(_list)

# heappush: 값을 힙에 넣음
heapq.heappush(_list, 7)

# heappop: heap에 있는 값중 최솟값을 뺌
print(heapq.heappop(_list))  # 7

# nsmallest: heap의 원소중 최솟값 n개 리턴
print(heapq.nsmallest(4, _list))  # [16, 31, 32, 54]

# nlargest: heap의 원소중 최댓값 n개 리턴
print(heapq.nlargest(4, _list))  # [94, 81, 54, 32]

# 최대 힙
# heappop 하는 경우 최댓값을 구할 수 있다.
# 튜플로 (음수로 변경한 값, 원래 값)으로 관리하여 최대 힙을 만들어서 사용
_list = [32, 16, 54, 94, 81, 31]
_list = [(-i, i) for i in _list]
heapq.heapify(_list)

# heappop: 최댓값 리턴
print(heapq.heappop(_list)[1])  # 94

# 자주 사용하는 라이브러리
# 내장 함수 : sum, min, max, sorted, zip
result = sum([1, 2, 3])
print(result)  # 6

result = min([1, 2, 3, 4, 5])
print(result)  # 1

result = max([1, 2, 3, 4, 5])
print(result)  # 5

result = sorted([1, 4, 10, 5, 0])
print(result)  # [0, 1, 4, 5, 10]

result = sorted([1, 4, 10, 5, 0], reverse=True)
print(result)  # [10, 5, 4, 1, 0]

# 튜플 2번째 값으로 정렬 하고자 할 경우 lamda식 사용
result = sorted([('lena', 10), ('jake', 2), ('ray', 5)], key=lambda x: x[1], reverse=True)
print(result)

# zip
_numbers = ['one', 'two', 'three']
_nums = [1, 2, 3]

_dict = dict(zip(_nums, _numbers))
print(_dict)  # {1: 'one', 2: 'two', 3: 'three'}
_list = list(zip(_nums, _numbers))
print(_list)  # [(1, 'one'), (2, 'two'), (3, 'three')]

# itertools: 조합, 순열 기능 제공하는 라이브러리
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['a', 'b', 'c']

# 순열 : 리스트에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
result = list(permutations(data, 2))
print(result)  # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

# 조합 : 리스트에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 경우를 계산
result = list(combinations(data, 2))
print(result)

# 데카르트 곱 : product는 순열 + 중복하여 뽑는 경우를 추가
result = list(product(data, repeat=2))
print(result)

_list = ["012", "abc", "!@#"]
pd = list(product(*_list))
print(pd)

# combinations_with_replacement는 조합 + 중복하여 뽑는 경우를 추가
result = list(combinations_with_replacement(data, 2))
print(result)

# bisect: 이진 탐색 기능을 제공하는 라이브러리
# bisect_left(a, x)	정렬된 a에 x를 삽입할 위치를 리턴, x가 이미 있는 경우는 x의 위치를 반환
# bisect_right(a, x) 정렬된 a에 x를 삽입할 위치를 리턴, x가 이미 있는 경우는 오른쪽(뒤)의 인덱스를 리턴
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]  # 정렬된 수
target = 4
print(bisect_left(a, target))  # 2
print(bisect_right(a, target))  # 4


# 원하는 수 인덱스 얻기
def binary_search(array=None, target=int()):
    """
    이진 탐색 -  bisect
    :param array:
    :param target:
    :return: target index
    """
    if array is None:
        array = list()
    index = bisect_left(array, target)
    if index < len(array) and array[index] == target:
        return index
    return None


array = [-1, 0, 3, 5, 9, 12]
print(binary_search(array=array, target=9))


# 범위에 있는 수의 데이터 개수 출력
def count_by_range(a, left_value, right_value):
    right_value = bisect_right(a, right_value)
    left_value = bisect_left(a, left_value)
    return right_value - left_value


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))  # 2
# 값이 -1 ~ 3인 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))  # 6

# Counter : Python이 제공하는 collections 라는 모듈의 한 class
# List를 가지고 Counter를 생성하면, Counter는 Key가 이름이고, Value가 count 인 dictionary를 반환
# Counter class는 상호간의 뺄셈 연산을 지원
from collections import Counter

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

_dict = Counter(participant) - Counter(completion)
print(_dict)
