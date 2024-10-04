import sys

input=sys.stdin.readline

def solv(N):
    phone_dict=set()
    phone_list=[input() for _ in range(N)]
    phone_list=sorted(phone_list)

    for phone_number in phone_list:
        for i in range(len(phone_number)):
            if phone_number[:i] in phone_dict:
                return 'NO'
        phone_dict.add(phone_number.rstrip())
    return 'YES'


T=int(input())

for _ in range(T):
    N=int(input())
    answer=solv(N)
    print(answer)


