import sys
from collections import deque


def bfs(start: int):
    queue = deque()
    queue.append(start)
    visited = [False] * 2 ** n
    level = 0

    while queue:
        r = len(queue)
        for _ in range(r):
            num = queue.popleft()
            if num == target:
                return level

            number = num ^ 3
            if not visited[number]:
                queue.append(number)
                visited[number] = True

            number = num ^ (3 << (n - 2))
            if not visited[number]:
                queue.append(number)
                visited[number] = True

            for di in range(n-2):
                number = num ^ (7 << di)
                if not visited[number]:
                    queue.append(number)
                    visited[number] = True

        level += 1

    return -1


n = int(sys.stdin.readline())
present = int(sys.stdin.readline(), base=2)
target = int(sys.stdin.readline(), base=2)

print(bfs(present))

# bin(n).lstrip('0b').zfill(n)
