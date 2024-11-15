N=int(input())
cost=[]
for _ in range(N):
    cost.append(list(map(int,input().split())))

dp=[[0]*N for _ in range(3)]

dp[0][0]=cost[0][0]
dp[1][0]=cost[0][1]
dp[2][0]=cost[0][2]

for i in range(1,N):
    dp[0][i]=min(dp[1][i-1]+cost[i][0],dp[2][i-1]+cost[i][0])
    dp[1][i]=min(dp[0][i-1]+cost[i][1],dp[2][i-1]+cost[i][1])
    dp[2][i]=min(dp[0][i-1]+cost[i][2],dp[1][i-1]+cost[i][2])
else:
    print(min(dp[0][N-1],dp[1][N-1],dp[2][N-1]))
