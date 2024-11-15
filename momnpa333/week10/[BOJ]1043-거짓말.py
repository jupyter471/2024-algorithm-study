import sys
input=sys.stdin.readline

N,M=map(int,input().split())
lier=set(list(map(int,input().split()))[1:])

parents=[i for i in range(N+1)]

groups=[]

def findparents(i):
    if i!=parents[i]:
        parents[i]=findparents(parents[i])
        return parents[i]
    return i

def union(a,b):
    a=findparents(a)
    b=findparents(b)
    if a in lier or b in lier:
        lier.add(a)
        lier.add(b)

    if a<b:
        parents[b]=a
    else:
        parents[a]=b

def islier(member):
    if findparents(member) in lier:
        return True
    return False

for _ in range(M):
    group_member=list(map(int,input().split()))[1:]
    groups.append(group_member)
    for member in group_member:
        union(member,group_member[0])
answer=0
for group in groups:
    for member in group:
        if islier(member):
            break
    else:
        answer+=1
print(answer)



