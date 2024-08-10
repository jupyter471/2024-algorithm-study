# N:듣도 못한 사람수, M:보도 못한 사람 수
# 듣 -> 보 순서대로 사람 이름
# 듣보 둘 다 있는 사람 숫자, 이름 순으로

n,m = map(int, input().split(" "))

d_set = set()
for _ in range(n):
    d_set.add(input())
b_set = set()
for _ in range(m):
    b_set.add(input())

db = d_set & b_set
print(len(db))
db = sorted(db)
for x in db:
    print(x)