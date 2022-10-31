'''
[문제] 		
    철수는 지금 모두의 마블 게임을 하고 있다.
    게임은 0 ~ 20까지 이동할 수 있는 거리가 있다.
    지금 철수의 차례이고 , 
    현재의 위치는 시작점으로부터 9만큼 이동했다.		 
    1 ~ 6의 눈금이 있는 주사위 2개를 던진다.
    주사위 숫자의 합만큼 이동한다. 
    아래 조건을 모두 만족하는 철수의 위치를 출력하시오.
        
    [조건]
    [1] 두 주사위 숫자가 서로 다를 경우는 현재위치에서
        주사위 숫자의 합만큼 이동한다. 
        예) 3, 5 ==> 8 만큼 이동한다.

    [2] 두 주사위 숫자가 같은 경우 보너스 이동 거리 6이 추가된다.
        예) 2, 2  ==> 4 + 6 만큼 이동한다.

    [3] 14, 15, 16 번의 위치에 함정이 있다. 
        함정에 걸리면 다시 주사위 2개를 던지고 
        그 합이 6이하이면 [페널티] 처음 위치(0)로 이동한다.
        그 합이 7이상이면 [페널티 없음] 함정을 탈출하여 다음 칸(17)으로 이동한다.

    [4] 20 이상의 값이 나오면 "승리"를 출력한다.
'''	

import random

cur_location = 9
print("start point", cur_location)

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print(dice1,dice2)

sum = dice1+dice2

## 선생님 풀이랑 다른 점! 나는 if 두개로 나눠서 푸는게 편하다!!
#dice1 != dice2
if dice1 != dice2:
    cur_location = 9 + sum
    print("diff",cur_location)
    

#dice1 == dice2
if dice1 == dice2:
    cur_location += 6
    print("same", cur_location)

#14,15,16
if cur_location == 14 or cur_location == 15 or cur_location == 16 :
    print("trap")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(dice1,dice2)
    
    sum = dice1+dice2
    ##under 6
    if sum <= 6:
        cur_location = 0
        print(cur_location)

    ##above 7
    if sum >= 7 :
        cur_location = 17
        print(cur_location)

# above 20
if cur_location >= 20:
    print("승리")     







'''
cur_location = 9
print("게임시작위치", cur_location)

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("주사위들 : ", dice1,dice2)


#주사위 숫자가 다를 경우
sum = dice1+ dice2                    #이렇게 먼저 선언해주면 주사위 숫자가 같은 경우만 따로 밑에 적어두면 된다!
cur_location = cur_location +sum
print("숫자달라",cur_location)

[오답]
dice1 != dice2:
    sum = dice1+dice2
    cur_location = 9 + sum
    print(cur_location)

#주사위 위치가 같은 경우
if dice1 == dice2 :
    sum += 6
    cur_location = 9 + sum
    print("숫자같아", cur_location)


#14,15,16에 걸릴 경우 
##중첩if문 :
if cur_location == 14 or cur_location == 15 or cur_location == 16 :
    print("함정에빠짐")
    dice1 = random.randint(1,6)       #여기서 다시 주사위 던지는거라 재정의
    dice2 = random.randint(1,6)
    print("함정주사위", dice1,dice2)

### 1) 6이하일 경우 
    if sum <= 6 :
        cur_location = 0 
        print("패널티", cur_location)

### 2) 7이상일 경우
    if sum >= 7 :
        cur_location = 17 
        print("패널티없음", cur_location)


# 20 이상의 값이 나올 경우
if cur_location >= 20 :
    print("승리")
'''