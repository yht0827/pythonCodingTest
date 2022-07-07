clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


def solution(clothes):
    hash = {}

    for k, v in clothes:
        if v in hash:
            hash[v] += 1
        else:
            hash[v] = 1

    answer = 1
    for k, v in hash.items():
        answer *= (v + 1)

    return answer - 1


# reduce, Counter 사용
def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


print(solution(clothes))

print(solution2(clothes))
