# 31120KB, 40ms


import sys


def solution():
    for party in parties:
        first = party[0]
        other = party[1:]
        for person in other:
            union(first, person)

    disjoint_set = set()
    for person in range(1, N+1):
        for known in known_people:
            if person == known or find(person) == find(known):
                break
        else:
            disjoint_set.add(person)

    count = 0
    for party in parties:
        for person in party:
            if person not in disjoint_set:
                break
        else:
            count += 1

    return count


def union(x, y):
    fx, fy = find(x), find(y)
    if fx != fy:
        people[fx] = fy


def find(prev):
    curr = people[prev]
    while people[curr] != curr:
        people[prev], curr = people[curr], people[curr]

    return curr


N, M = map(int, sys.stdin.readline().split())

people = [i for i in range(N+1)]
known_people = list(map(int, sys.stdin.readline().split()))[1:]
parties = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(M)]

print(solution())
