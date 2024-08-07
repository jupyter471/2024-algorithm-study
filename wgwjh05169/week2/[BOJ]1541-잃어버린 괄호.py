import sys
import re

input = sys.stdin.readline


def find_minimum(string):
    tokens = re.split("(-|\+)", string.rstrip())

    stack = []
    for token in tokens:
        if len(stack) > 1 and stack[-1] == '+':
            op = stack.pop()
            num1 = stack.pop()
            stack.append(int(num1) + int(token))
        else:
            stack.append(token)

    ans = int(stack[0])
    for token in stack[1:]:
        if token != '-':
            ans -= int(token)

    return ans


print(find_minimum(input()))
