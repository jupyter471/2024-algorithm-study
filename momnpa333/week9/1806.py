N,S=map(int,input().split())

seq=list(map(int,input().split()))


left=0; right=0
cur=seq[0]
answer=len(seq)*2
while left<=right:
    if cur<S and right<len(seq)-1:
        right+=1
        cur+=seq[right]
    elif cur>=S:
        if right-left+1<answer:
            answer=right-left+1
        cur-=seq[left]
        left+=1
    else:
        break
if answer==len(seq)*2:
    print(0)
else:
    print(answer)