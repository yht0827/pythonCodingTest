id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)

    for re in report:
        re = re.split()
        user[re[0]].add(re[1])
        cnt[re[1]] += 1

    for i in id_list:
        result = 0
        for j in user[i]:
            if cnt[j] >= k:
                result += 1
        answer.append(result)

    return answer


def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


print(solution(id_list, report, k))
print(solution2(id_list, report, k))
