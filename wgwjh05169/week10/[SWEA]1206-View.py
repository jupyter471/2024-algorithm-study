def search():
    N = int(input())
    heights = list(map(int, input().split()))
 
    count = 0
    for i in range(2, N - 2):
        maximum_neighbor = max(*heights[i - 2:i], *heights[i + 1:i + 3])
        if heights[i] > maximum_neighbor:
            count += heights[i] - maximum_neighbor
 
    return count
 
 
for t in range(1, 11):
    result = search()
    print(f"#{t} {result}")
