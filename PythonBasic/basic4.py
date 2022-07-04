# 튜플 자료 형
# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 리스트는 대괄호([ ])를 이용 하지만, 튜플은 소괄호(( ))를 이용
# 해당 자료 형은 그래프 알고리즘을 구현할 때 자주 사용
# 다익스트라 최단 경로를 찾아주는 알고리즘의 내부에서 우선순위 큐를 사용

a = (1, 2, 3, 4)
print(a)
# a[2] = 7  # TypeError: 'tuple' object does not support item assignment

# dict 자료형 {}
#  시간 복잡도 : 삭제 O(1), 삽입 O(1), 검색 O(1)

# dict 정의
data = {'apple': '사과', 'banana': '바나나'}
print(data)  # {'apple': '사과', 'banana': '바나나'}

# 특정 키 존재 확인
if 'apple' in data:
    print('사과가 존재함')

# 삭제
del data['apple']
print(data)  # {'banana': '바나나'}

# 추가 및 수정
data['apple'] = '사과'

# dict 키, 값들 얻기
key_list = data.keys()
val_list = data.values()
print(key_list)  # dict_keys(['apple', 'banana'])
print(val_list)  # dict_values(['사과', '바나나'])

# dict for문 - key만 얻기
for key in key_list:
    print(data[key])  # 사과 바나나

# dict for문 - key, vlaue 모두 얻기
for k, v in data.items():
    print(k, v)

# zip으로 딕셔너리로 만들기
_number = ['one', 'two', 'three']
_num = [1, 2, 3]
_dict = dict(zip(_number, _num))
print(_dict)  # {'one': 1, 'two': 2, 'three': 3}

# dict sort
_dict = {'one': 1, 'two': 2, 'three': 3}
# 키 기준 정렬 -> 영어 사전순
print(sorted(_dict.items()))  # [('one', 1), ('three', 3), ('two', 2)]

# 값 기준 정렬
print(sorted(_dict.items(), key=(lambda x: x[1])))  # [('one', 1), ('two', 2), ('three', 3)]

# setdefault()를 이용하면 한 줄로 가능 더 간편한 방법은 아래 defaultdict를 사용
_dict = dict()

# 첫 번째 인자가 존재하지 않는 경우 "고양이"로 값을 세팅
print(_dict.setdefault('cat', '고양이'))  # 고양이

# 기존에 해당 키가 이미 존재하면 세팅을 안함
_dict = {'cat': '고양이'}
print(_dict.setdefault('cat', "고냥이"))  # 고양이

# 자주 사용하는 딕셔너리 모듈 - defaultdict 객체
import collections  # defaultdict 사용하기 위한 모듈

default_dict = collections.defaultdict(int)  # int로 디폴트 dict 생성
default_dict['a']
default_dict['b'] += 1  # 기본값 0에 +1
print(default_dict)  # defaultdict(<class 'int'>, {'a': 0, 'b': 1})

# 자주 사용하는 딕셔너리 모듈 - Counter 객체
# 동일한 값이 몇 개가 존재하는지 dict 형식으로 리턴해준다. 아래의 예제를 보면 알파벳 값이 몇 개 있는지 출력 해준다.
a = ["a", "b", "c", "a", "b", "b"]
counter_dict = collections.Counter(a)
print(counter_dict)  # Counter({'b': 3, 'a': 2, 'c': 1})
print(type(counter_dict))  # <class 'collections.Counter'>
print(counter_dict.most_common(2))  # 상위 2개 리턴. [('b', 3), ('a', 2)]
print(counter_dict.most_common(1)[0][0])  # 가장 우선 순위가 높은 것. (key)  b

# 집합 자료형
# 중복을 허용 하지 않는다, 순서가 없다.
# 초기화 방법
data = {1, 1, 2, 3, 4, 4, 5}
print(data)  # {1, 2, 3, 4, 5}

data = {1, 1, 2, 3, 4, 4, 5}
print(data)  # {1, 2, 3, 4, 5}

# 집합 자료 형의 연산
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)  # 합집합. {1, 2, 3, 4, 5, 6, 7}
print(a & b)  # 교집합. {3, 4, 5}
print(a - b)  # 차집합. {1, 2}

# set 자료형 관련 자주 사용 되는 함수
data = {1, 2, 3}
print(data)  # {1, 2, 3}

# 추가
data.add(4)
print(data)  # {1, 2, 3, 4}

# 업데이트
data.update([5, 6])
print(data)  # {1, 2, 3, 4, 5, 6}

# 삭제
data.remove(3)
print(data)  # {1, 2, 4, 5, 6}
