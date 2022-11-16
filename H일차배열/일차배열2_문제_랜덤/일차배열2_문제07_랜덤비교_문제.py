'''
    [문제]
        [조건1] a, b 리스트 두 개에 1~100 사이의 랜덤 값 다섯 개를 저장한다.
        [조건2] base 변수에 랜덤으로 1~100 사이의 숫자를 저장한다. 
        base 변수값보다 큰 값들을 전부 출력하시오.
    [예시]
'''

a = []
b = []

base = 0



import random
i = 0
while i < 5:
    r1 = random.randint(1,100)
    r2 = random.randint(1,100)
    r3 =random.randint(1,100)
    a.append(r1)
    b.append(r2)
    base = 73

    if a[i] > base :
        print("a :",a[i])
    if b[i] >base :
        print("b :",b[i])
    i += 1
print("base :",base)
print("a =",a,"b =",b)


