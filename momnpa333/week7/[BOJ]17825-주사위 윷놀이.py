import sys
from collections import deque
import copy
input=sys.stdin.readline

rolls=list(map(int,input().split()))

#10->25 :A
#20->25: B
#30->25: C
#25->40: D
#그외 :S
Sboard=[[i,True] for i in range(0,40,2)]
Aboard=[[i,True] for i in range(10,22,3)]
Bboard=[[i,True] for i in range(20,26,2)]
Cboard=[[i,True] for i in range(28,25,-1)]
Dboard=[[i,True] for i in range(25,45,5)]

#말->W,X,Y,Z
total_score={
    "W":0,
    "X":0,
    "Y":0,
    "Z":0
}

def move_horse(horse,position,dice,total_score,Sboard,Aboard,Bboard,Cboard,Dboard):
    if position[0]=="S":
        if dice+position[1]>20:
            Sboard[dice+position[1]][1]=True
            return ("EXIT",total_score)
        if dice+position[1]==5 and Aboard[0][1]==True:
            total_score[horse]+=Aboard[0][0]
            Sboard[position[1]][1]=True
            Aboard[0][1]=False
            return ("A",0,total_score)
        if dice+position[1]==10 and Bboard[0][1]==True:
            total_score[horse]+=Aboard[0][0]
            Sboard[position[1]][1]=True
            Bboard[0][1]=False
            return ("B",0,total_score)
        if dice+position[1]==15 and Cboard[0][1]==True:
            total_score[horse]+=Aboard[0][0]
            Sboard[position[1]][1]=True
            Cboard[0][1]=False
            return ("C",0,total_score)
        if dice+position[1]==20 and Dboard[3][1]==True:
            total_score[horse]+=Dboard[3][0]
            Sboard[position[1]][1]=True
            Dboard[3][1]=False
            return ("D",3,total_score)
        if Sboard[dice+position[1]][1]==True:
            total_score[horse]+=Sboard[dice+position[1]][0]
            Sboard[position[1]][1]=True
            Sboard[dice+position[1]][1]=False
            return ("S",dice+position[1],total_score)
        return ("S",position[1],total_score)
    if position[0]=="A":
        next_position=dice+position[1]
        if next_position>7:
            Aboard[position[1]]=True
            return ("EXIT",total_score)
        if next_position>3:
            next_position-=4
            if Dboard[next_position][1]==True:
                total_score[horse]+=Dboard[next_position][0]
                Dboard[next_position][1]=False
                Aboard[position[1]][1]=True
                return ("D",next_position,total_score)
        if Aboard[next_position][1]==True:
            total_score[horse]+=Aboard[next_position][0]
            Aboard[next_position][1]=False
            Aboard[position[1]]=True
            return ("A",next_position,total_score)
    if position[0]=="B":
        next_position=dice+position[1]
        if next_position>6:
            Bboard[position[1]]=True
            return ("EXIT",total_score)
        if next_position>2:
            next_position-=3
            if Dboard[next_position][1]==True:
                total_score[horse]+=Dboard[next_position][0]
                Dboard[next_position][1]=False
                Bboard[position[1]][1]=True
                return ("D",next_position,total_score)
        if Bboard[next_position][1]==True:
            total_score[horse]+=Bboard[next_position][0]
            Bboard[next_position][1]=False
            Bboard[position[1]]=True
            return ("B",next_position,total_score)
    if position[0]=="C":
        next_position=dice+position[1]
        if next_position>7:
            Cboard[position[1]]=True
            return ("EXIT",total_score)
        if next_position>3:
            next_position-=4
            if Dboard[next_position][1]==True:
                total_score[horse]+=Dboard[next_position][0]
                Dboard[next_position][1]=False
                Cboard[position[1]][1]=True
                return ("D",next_position,total_score)
        if Cboard[next_position][1]==True:
            total_score[horse]+=Cboard[next_position][0]
            Cboard[next_position][1]=False
            Cboard[position[1]]=True
            return ("C",next_position,total_score)
    if position[0]=="D":
        next_position=dice+position[1]
        if next_position>3:
            Dboard[position[1]]=True
            return ("EXIT",total_score)
        if Dboard[next_position][1]==True:
            total_score[horse]+=Dboard[next_position][0]
            Dboard[next_position][1]=False
            Dboard[position[1]]=True
            return ("D",next_position,total_score)
    return (position[0],position[1],total_score)


dq=deque([])
dq.appendleft(({"W":("S",0),"X":("S",0),"Y":("S",0),"Z":("S",0)},total_score.copy(),copy.deepcopy(Sboard),copy.deepcopy(Aboard),copy.deepcopy(Bboard),copy.deepcopy(Cboard),copy.deepcopy(Dboard)))
round=0
while dq:
    if round==1:
        break
    for _ in range(len(dq)):
        horses,total_score,Sboard,Aboard,Bboard,Cboard,Dboard=dq.popleft()
        for horse in horses:
            result=move_horse(horse,horses[horse],rolls[round],total_score,Sboard,Aboard,Bboard,Cboard,Dboard)
            horse_status=horses.copy()
            if result[0]=="EXIT":
                del horse_status[horse]
                dq.appendleft((horse_status,result[1],copy.deepcopy(Sboard),copy.deepcopy(Aboard),copy.deepcopy(Bboard),copy.deepcopy(Cboard),copy.deepcopy(Dboard)))
                continue
            horse_status[horse]=(result[0],result[1])
            dq.appendleft(((horse_status),result[2],copy.deepcopy(Sboard),copy.deepcopy(Aboard),copy.deepcopy(Bboard),copy.deepcopy(Cboard),copy.deepcopy(Dboard)))
    round+=1

for item in dq:
    print(item[0],item[1])



