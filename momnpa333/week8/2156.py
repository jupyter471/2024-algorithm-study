import sys
input=sys.stdin.readline

N=int(input())

wine=[]
for _ in range(N):
    wine.append(int(input()))

if N<3:
    print(sum(wine))
    exit(0)

dp=[0]*N

dp[0]=wine[0]
dp[1]=dp[0]+wine[1]
dp[2]=max(dp[1],dp[0]+wine[2],wine[1]+wine[2])

for i in range(3,N):
    dp[i]=max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])

print(dp[-1])