# 16236 - 아기상어
# memory: 34140 KB, times: 140 ms, lang: python3 
# BFS 

import sys
from collections import deque

grid_size = int(input()) 
space = []
for col in range(grid_size):
    space.append(list(map(int, input().split())))
    for row in range(grid_size):
        if space[col][row] == 9:  
            shark_y, shark_x = col, row
            space[col][row] = 0  

delta_x, delta_y = [1, 0, -1, 0], [0, 1, 0, -1]
baby_shark_size = 2  

def search_path():
    distance_map = [[-1] * grid_size for _ in range(grid_size)]
    distance_map[shark_y][shark_x] = 0
    q = deque([(shark_y, shark_x)])
    
    while q:
        curr_y, curr_x = q.popleft()
        for i in range(4):
            next_y, next_x = curr_y + delta_y[i], curr_x + delta_x[i]
            if 0 <= next_y < grid_size and 0 <= next_x < grid_size:
                if distance_map[next_y][next_x] == -1 and space[next_y][next_x] <= baby_shark_size:
                    distance_map[next_y][next_x] = distance_map[curr_y][curr_x] + 1
                    q.append((next_y, next_x))
    
    return distance_map

def find_prey(distance_map):
    min_distance = float('inf')
    target_y, target_x = -1, -1
    
    for col in range(grid_size):
        for row in range(grid_size):
            if 1 <= space[col][row] < baby_shark_size and distance_map[col][row] != -1:
                if distance_map[col][row] < min_distance:
                    min_distance = distance_map[col][row]
                    target_y, target_x = col, row

    if min_distance == float('inf'):
        return -1, -1, -1
    else:
        return target_y, target_x, min_distance

total_time = 0
eaten_count = 0

while True:
    res = find_prey(search_path())
    prey_y, prey_x, distance_to_prey = res

    if prey_y == -1:
        print(total_time) 
        break
    
    shark_y, shark_x = prey_y, prey_x
    total_time += distance_to_prey 
    space[shark_y][shark_x] = 0  
    eaten_count += 1  
    
    if eaten_count >= baby_shark_size:
        baby_shark_size += 1
        eaten_count = 0
