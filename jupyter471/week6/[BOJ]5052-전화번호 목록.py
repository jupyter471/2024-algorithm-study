"""
전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자

긴급전화: 911
상근: 97 625 999
선영: 91 12 54 26
이 경우에 선영이에게 전화를 걸 수 있는 방법이 없다. 전화기를 들고 선영이 번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다. 따라서, 이 목록은 일관성이 없는 목록이다.
전화번호의 길이는 길어야 10자리
"""

def main():
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        if check(n):
            print("YES")
        else:
            print("NO")

def check(n):
    phone_book = [input() for _ in range(n)]
    phone_book = sorted(phone_book)
    for phone_number1, phone_number2 in zip(phone_book, phone_book[1:]):
        if phone_number2.startswith(phone_number1):
            return False
    return True

main()
