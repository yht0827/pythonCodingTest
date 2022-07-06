participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant) - 1]


print(solution(participant, completion))

# Counter를 활용
from collections import Counter


def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


# Hash를 활용
def solution3(participant, completion):
    hash_dict = {}
    sum_hash = 0

    for part in participant:
        hash_dict[hash(part)] = part
        sum_hash += hash(part)

    for comp in completion:
        sum_hash -= hash(comp)

    return hash_dict[sum_hash]


print(solution3(participant, completion))
