'''
    [문제]
        1부터 10 사이의 랜덤 숫자 두 개를 출력한다.
        하나는 반드시 1~5 사이의 숫자이어야 하고,
        나머지 하나는 반드시 6~10 사이의 숫자이어야 한다.
        출력순서도 랜덤으로 출력되어야 한다. 

        [예1]
            3, 6
        [예2]
            8, 1

'''



import random

a = random.randint(1,5)
b = random.randint(6,10)

#print(a,b)

num1 = random.randint(1,2)


if num1 == 1:
    print(a,b)

if num1 == 2:
    print(b,a)


