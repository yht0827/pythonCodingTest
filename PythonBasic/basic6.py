# 정렬
"""
 1. sorted 함수 사용
"""
array = [7, 5, 9, 0, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)  # [0, 1, 2, 4, 5, 6, 7, 8, 9]

"""
 2. sort 메소드 사용 - 리스트 변수 
"""
array = [7, 5, 9, 0, 1, 6, 2, 4, 8]

array.sort()
print(array)  # [0, 1, 2, 4, 5, 6, 7, 8, 9]

"""
 3. sort함수 - 람다 
"""
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort(key=lambda x: x[0])  # Stable Sort (When using a key)
print(data)

"""
4. 정렬 여러개하는 경우
"""
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
s = sorted(data, key=lambda x: (x[0], x[1]))
print(s)

# bfs
from collections import deque


def bfs(graph, visited, start):
    dq = deque([start])
    visited[start] = True

    while dq:
        now = dq.popleft()
        print(now, end=" ")
        for next in graph[now]:
            if not visited[next]:
                dq.append(next)
                visited[next] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)
bfs(graph, visited, 1)

# https://ryu-e.tistory.com/72?category=899990
