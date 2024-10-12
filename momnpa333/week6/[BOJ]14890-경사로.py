import sys
input=sys.stdin.readline


N,L=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]

def is_flat(list):
    for item in list:
        if list[0]!=item:
            return False
    return True

def is_possible(list):
    check=set()
    start=0;end=start+L
    while True:
        if end>=N:
            if is_flat(list[start:]):
                return True
            else:
                return False
        if abs(list[start]-list[end])>1:
            return False
        
        if list[start]-list[end]==-1: ## 오르막
            if is_flat(list[start:end]):
                for i in range(start,end):
                    if i not in check:
                        check.add(i)
                    else:
                        return False
                start=end; end=start+L
            else:
                return False
        elif list[start]-list[end]==1: ##내리막
            if is_flat(list[start+1:end+1]):
                for i in range(start+1,end+1):
                    if i not in check:
                        check.add(i)
                    else:
                        return False
                start=end; end=start+L  
            else:
                start+=1; end=start+L
        elif abs(list[start]-list[end])==0: ## 평지
            if is_flat(list[start:end+1]):
                start+=1; end=start+L
            else:
                return False


            



def solve():
    answer=0

    for row in board:
        if(is_possible(row)):
            answer+=1
    
    rotate_board=zip(*board)
    
    for col in rotate_board:
        if(is_possible(col)):
            answer+=1

    return answer


answer = solve()

print(answer)