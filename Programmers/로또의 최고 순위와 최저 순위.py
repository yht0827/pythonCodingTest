lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]


def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]

    zero = lottos.count(0)
    ans = 0
    for lo in lottos:
        if lo in win_nums:
            ans += 1

    return answer[zero + ans], answer[ans]


print(solution(lottos, win_nums))
