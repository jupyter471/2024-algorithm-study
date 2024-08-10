"""
+,-로 이루어진 식에 () 넣어서 최소 식
0~9,+,-
가장 작은 값에서 가장 큰 값을 빼면 됨

55-(50+40)
1. 더할 수 있는 거 더해주고
2. 순서대로 빼면 됨


"""
formula = input()
split_form = formula.split("-")
num_list = []
for x in split_form:
    sum = 0
    p_split = x.split("+")
    for i in p_split:
        sum += int(i)
    num_list.append(sum)
result = num_list[0]
for i in num_list[1:]:
    result -= i
print(result)

#메모리 너무 많이 씀!