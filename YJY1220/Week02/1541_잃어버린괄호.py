# BOJ - 1541.잃어버린 괄호
# memory: 31120 KB , times: 36ms, lang: python
# '-' 기준 나눔 -> 첫번째 모두 더함, 나머지 뺌
# 이후 '-' 뒤에 모조리 뺌 


N = input()  

num = N.split('-')

first = num[0]  
fir_num = first.split('+')  
min_sum = 0  

for i in fir_num:
    min_sum += int(i)  

for j in num[1:]:
    numbers = j.split('+')  
    numbers_sum = 0  

    for i in numbers:
        numbers_sum += int(i)  
    min_sum -= numbers_sum  

print(min_sum)
