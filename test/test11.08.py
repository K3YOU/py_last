"""
    [문제]
        철수는 볼펜을 (10~30)개를 구입해야 한다. 
        
        볼펜 하나의 가격은 1200원이다. 	
        볼펜은 20개 이상 구매 시 볼펜 한 개에 100원을 할인해주고 있다. 
            
        또한, 회원 등급에 따라 할인을 추가 제공한다.
        
        회원 등급이 1이면  볼펜한개에 150원 할인 
        회원 등급이 2이면  볼펜한개에 50원 할인
        기본회원 등급은 3이고 할인을 제공하지 않는다.
        위 개수에따른 할인과 중복적용된다. 

        볼펜 수를 랜덤으로 저장한다.
        회원 등급을 랜덤으로 저장한다. 
        
        철수가 지급해야 하는 금액을 출력하시오.
        

    [예시]
        볼펜 10 , 회원등급1 => 1050 * 10
        볼펜 20 , 회원등급1 => 950 * 20
        볼펜 15 , 회원등급2 => 1150 * 15
        볼펜 20 , 회원등급2 => 1050 * 20

"""
import random
a = random.randint(10,30) #pen count
print("펜개수 :",a)
pen = 1200
pen_amount = 20
pen_per_dis = 100
#total = 0
b= random.randint(1,3) #degree
print("등급 :",b)

if a < 20 : 
    if b == 1 :
        pen1 = pen - 150
    if b == 2 :
        pen1 = pen - 50
    if b == 3 :    
        pen1 = pen
    total = pen1 * a
    print("total :",total)

if a >= 20 :
    if b == 1 :
        pen1 = pen - pen_per_dis - 150 
    if b == 2 :
        pen1 = pen - pen_per_dis - 50 
    if b == 3 :
         pen1 = pen - pen_per_dis
   
    total = a * pen1
    print("total :",total)



print("=================================================")

"""
    [문제]
        50~100 사이의 랜덤값을 저장하고 그값의 약수를 전부 구하고, 
        그약수의 가운데 위치의 값만 출력한다. 
        만약에 약수의 개수가 짝수이면 가운데값 두개중 앞의 값을 출력한다. 
    [예시]
        50 => 1, 2, 5, 10, 25, 50 총 6개이므로 5 , 10 이 가운데 값들이고,  그 중 앞의 값 5를 출력한다. 
    [예시]
        51 => 1, 3, 17 총 3개 이므로 3만 출력한다. 
"""

import random
a= random.randint(50,100)
print("a",a)

run = 1
b= 0
i = 1
count = 0
while run == 1 :
    if i <= a and a % i == 0 :
        print(i)
        count += 1
        if count % 2 == 0 :
            b = (count // 2) -1 
        run = 0 
    i += 1    

#################################################################################
print('문제2')
num = random.randint(50, 100)
print('랜덤숫자', num)
i = 1

count1 = 0 #약수의 개수 카운트
while i <= num:
    if num % i == 0: 
        count1 += 1
    i += 1

check = 0 #약수 개수 홀짝 구분
if count1 % 2 == 0:  #짝수이면
    check = count1 // 2 
else:                 #홀수이면
    check = count1 // 2 + 1 
    
i = 1
count2 = 0
result= 0
while i <= num:
    if num % i == 0:
        count2 += 1

    if count2 == check:
        result = i
        i = num + 1
    i += 1
print(result)