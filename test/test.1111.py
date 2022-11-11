"""
    [문제]
    [내마음대로 주사위게임]
        내마음대로 주사위게임 은 a와 b가 주사위를 두개를 던진다.
        두개의 주사위중 하나를 랜덤으로 선택해서 제시한다. 

        아래의 특별한 게임규칙에 따라 승패가 갈린다. 
    
        a는 주사위를 2개 던진다.
        b는 주사위를 2개 던진다.

        a와 b는 두 주사위중 하나를 랜덤 선택해서 제출한다. 

        <게임규칙>
            [1] 숫자가 둘다 짝수이면 둘중 큰수가 승리 , 숫자가 같으면 비김
            [2] 숫자가 둘다 홀수이면 둘중 작은수가 승리 , 숫자가 같으면 비김
            [3] 하나는 짝수이고 하나는 홀수이면 
                주사위 숫자와 상관없이 비긴다. 
"""
import random
#두개의 주사위가 있고
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("dice1 :",dice1,"dice2 :",dice2)

dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
print("dice3 :",dice3,"dice4 :",dice4)

run = 1
while run == 1:
    #주사위 하나를 랜덤으로 선택

    #a가 주사위 고르기
    a = random.randint(1,2)
    print("a :",a)
    if a == 1:
        a_dice = dice1
        print(a_dice ,"from dice1(a)")

    if a == 2:
        a_dice = dice2
        print(a_dice,"from dice2(a)")

    #b가 주사위 고르기
    b = random.randint(1,2)
    print("b :",b)
    if b == 1:
        b_dice = dice3
        print(b_dice,"from dice3(b)")

    if b == 2:
        b_dice = dice4
        print(b_dice,"from dice4(b)")

    #홀짝
    if (a_dice % 2 != 0 and b_dice % 2 == 0)or (a_dice % 2 == 0 and b_dice % 2 != 0) :
        print("tie ")

    #짝수
    if a_dice % 2== 0 and b_dice % 2 == 0 :
        if a_dice > b_dice :
            print("result(even) : a win : ",a_dice) 
        if b_dice > a_dice :
            print("result(even) : b win : ",b_dice) 
        if a_dice == b_dice :
            print("tie as same") 
            
    #홀수
    if a_dice % 2!= 0 and b_dice % 2 != 0 :
        if a_dice > b_dice :
            print("result(odd) : a win : ",a_dice) 
        if b_dice > a_dice :
            print("result(odd) : b win : ",b_dice) 
        if a_dice == b_dice :
            print("tie as same") 
    run = 0

"""
    [문제]
        반복문을 활용해서 1~99까지 반복한다.
        1~99사이의 숫자중에서 4 와 8 의 개수를 출력하시오.
    [정답]
        40
"""

i = 1
count = 0
sum = 0
while i <= 99 :
    ten = i // 10
    one = i % 10

    #십의 자리에 4,8이 있는 경우
    if ten == 4 :
        count += 1
    if ten == 8 :
        count += 1
    #일의 자리에 4,8이 있는 경우
    if one == 4 :
        count += 1
    if one == 8 :
        count += 1
    i += 1    
    sum += count
print("==================2번문제===============================")
print(count)