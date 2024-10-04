# 42380KB, 924ms

import sys


class Node:
    value: str
    child: list

    def __init__(self, v):
        self.value = v
        self.child = []


def case():
    N = int(sys.stdin.readline())

    phones = []
    for _ in range(N):
        phones.append(sys.stdin.readline().rstrip())
    phones.sort(key=lambda x: -len(x))

    trie = [Node('root')]
    for phone in phones:
        if find_prefix(trie, phone):
            return 'NO'

    return 'YES'


def find_prefix(trie, phone):
    curr = trie[0]
    for i, ch in enumerate(phone):
        flag = True
        for child in curr.child:
            if child.value == ch:
                curr = child
                flag = False
                break

        if flag:
            curr.child.append(Node(ch))
            curr = curr.child[-1]

        if i == len(phone) - 1:
            if not flag:
                return True

    return False


T = int(sys.stdin.readline())
for _ in range(T):
    print(case())
