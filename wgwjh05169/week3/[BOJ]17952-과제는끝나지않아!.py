# memory: 109940KB, time: 988ms

import sys

input = sys.stdin.readline

stack = []
done = 0

n = int(input())
for _ in range(n):
    assignment = input()
    if assignment[0] == '1':
        stack.append(list(map(int, assignment.lstrip("1").lstrip(" ").split(" "))))

    if not stack:
        continue

    stack[-1][1] -= 1
    if stack[-1][1] == 0:
        score, cnt = stack.pop()
        done += score

print(done)
