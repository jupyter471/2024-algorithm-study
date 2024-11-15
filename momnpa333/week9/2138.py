N=int(input())

origin=list(input())
target=list(input())
answer = len(origin)*2 
def turn_light(switch_list,lights):
    for switch in switch_list:
        if lights[switch]=='0':
            lights[switch]='1'
        else:
            lights[switch]='0'
    return lights

def solve(position,cur,count):
    global answer
    off_lights=cur[:]
    on_lights=[]
    if position==0:
        switch_list=[position,position+1]
        on_lights=turn_light(switch_list,cur[:])
    elif position==len(cur)-1:
        switch_list=[position-1,position]
        on_lights=turn_light(switch_list,cur[:])
    else:
        switch_list=[position-1,position,position+1]
        on_lights=turn_light(switch_list,cur[:])


    if off_lights==target:
        if answer>count:
            answer=count
            return
    if on_lights==target:
        if answer>count+1:
            answer=count+1
            return

    if 1<position<len(cur)-1:
        if target[position-2]==cur[position-2]:
            solve(position+1,off_lights,count)
            solve(position+1,on_lights,count+1)
    elif position==0:
        solve(position+1,off_lights,count)
        solve(position+1,on_lights,count+1)
    elif position==1 and len(cur)!=2:
        solve(position+1,off_lights,count)
        solve(position+1,on_lights,count+1)
solve(0,origin,0)

if answer==len(origin)*2:
    print(-1)
else:
    print(answer)
