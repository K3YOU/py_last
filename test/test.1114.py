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

    a 와 b는 위 게임을 무한으로 반복한다. 
    둘중 한명이 연속으로 3번 승리하면 게임 종료.    
    과정을 전부 출력한다. 
"""
#틀린이유!
#연속적으로 : 하나는 +일 때 나머지는 0으로 만들기
## count_a += 1 이면 count_b = 0 이어야 연속적인 승리를 기록할 수 있다
#a,b가 두 주사위 중 하나(0,1)를 고르고나서 주사위에서 나온 숫자(dice1,dice2)를 정의할 수 있는 새로운 변수를 써줘야한다. =>final_a , final_b


import random


#a 와 b가 주사위를 두번 던진다

count_a = 0
count_b = 0

run = 1
while run == 1 :
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    a = random.randint(0,1)
    if a == 0 :
        print("a :", dice1)
        final_a = dice1
    else :
        print("a :", dice2)
        final_a = dice2


    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    b = random.randint(0,1)
    if b == 0 :
        print("b :", dice1)
        final_b = dice1
    else :
        print("b :", dice2)
        final_b = dice2

    #both even
    if final_a % 2 == 0 and final_b % 2 == 0 :
        if a == b :
            count_b = 0
            count_a = 0
            print("tie")
        if final_a > final_b :
            print("a wins in even")
            count_b += 1
            count_a = 0

            
        if final_a < final_b :
            print("b wins in even")
            count_a += 1
            count_b  = 0

    #both odd
    if final_a % 2 != 0 and final_b  % 2 != 0 :
        if final_a == final_b :
            print("tie")
            count_b= 0
            count_a = 0
        if final_a > final_b :
            print("b wins in odd")
            count_a += 1
            count_b = 0

            

        if final_a < final_b :
            print("a wins in odd")
            count_b += 1
            count_a = 0
      

    #both diff
    #a is odd
    if final_a % 2 != 0 and final_b % 2 == 0 :
        print("tie in diff")
        count_b= 0
        count_a = 0
    # b is odd
    if final_a % 2 == 0 and final_b % 2 != 0 :
        print("tie in diff")
        count_b= 0
        count_a = 0

    if count_a == 3:
        print("a's victory")
        run = 0

    if count_b == 3:
        print("b's victory")
        run = 0
    
    
   
