"""
[문제]
	철수는 농구공을 18번던저 11번 성공했다.
	철수의 성공 확률을 출력하시오.
    소수점 2자리로 구하시오.
"""

print("1번 문제")
chul = 11/18 * 100
print(round(chul,2))

"""
[문제]
	철수는 12초에 100미터를 달린다.
	철수의 시속을 구하시오. 
	단, 철수는 일정한속도로 달린다.
    소수점 2자리로 구하시오.
"""
print("2번문제")
sec = 12
distance = 100

speed_per_hour = (distance/sec)*3600
print(round(speed_per_hour,2))
'''

12: 100 = 3600 : x
360000 = 12x
x = 360000/12
12x= 100
x = 100/12% 3600

'''



"""
[문제]
    1부터 100사이의 랜덤숫자를 변수a에 저장한다. 
    a의 값이 1~5사이면 b에 95 저장후 출력
    a의 값이 6~10사이면 b에 90 을저장후 출력       
    a의 값이 11~15사이면 b에 85 를저장후 출력
    ....
    ....
    a의 값이 91~95 사이면 b에 5를 저장후 출력
    a의 값이 96~100 사이면 b에 0을 저장후 출력 
"""  #2=> 2% 5 
print("3번문제")
import random
a = random.randint(1,100)

c = (a // 5) +1
if a % 5 == 0:
    c = a//5
b = 100 -5*c
print(a,b)
    




"""
[문제]	
	자동차 카센터에는 수리를 기다리는 오토바이와 자동차가 있다.
	오토바이와 자동차를 합쳐서 21대가 있다.
	바퀴는 합쳐서 70개 일때 오토바이와 자동차의 대수를 구하시오.
"""
print("4번문제")
print("자동차",14,"오토바이",7)
'''
오토바이바퀴수 = 2x
자동차바퀴수 = 4y
2x+4y = 70
2x+2y = 42

2y = 28
y = 14
x =7

'''
"""
[문제] 
    1000보다 큰 수중에서 12의 배수를 검색하고, 
    십의자리가 4인 수를
    가장 작은 수부터 차례대로 4개를 출력하시오. 
"""
print("5번문제")

count = 0
b = 1001
run = 1
while run == 1 :
    if b % 12 == 0 and b % 100 // 10 == 4 :
        print(b)
        count += 1
    if count == 4 :
        run = 0
    b += 1


"""
[문제]
    100 ~ 999 사이의 숫자를 랜덤으로 3개 출력한다. 
    단, 전부 각각의숫자마다 숫자5가 한개이상 포함되어야한다.
[예시]
    145
    536
    955
"""
print("6번 문제")
import random

run = 1
count = 0
while run == 1:
    
    r1 =random.randint(100,999)

    백 = r1 // 100
    십 = r1 % 100 // 10
    일 = r1 % 10

    if 백 == 5 or 십 == 5 or 일 ==5 :
        print(r1)
        count += 1
        if count == 3:
            run = 0 



"""
[문제]
    a = [] 
    a리스트에 1~5사이의 랜덤숫자 15개를 저장한다.
    숫자 1 2 3 이 연속으로 나오면 당첨이라고 할때,
    당첨이 몇번나왔는지 출력하시오.
[예시]

    a = [1, 5, 2, 1, 2, 3, 3, 2, 1, 4, 1, 2, 3, 4, 2] 
    당첨: 2번
"""

print("7번문제")
import random
a=[]
i =0
count = 0
jackpot = 0
for i in range(15):  #for문 2개쓰기 : 첫 for문은 a 배열 만들어주는 용
    r= random.randint(1,3)
    a.append(r)
print(a)       


for i in range(len(a)-2):    #len(a) 라고 써주면 안된다/ i는 마지막까지 돌리면 i+2가 들어갈 자리가 없다.
    if a[i] == 1 :
        
        if a[i+1] == 2:
            
            if a[i+2] == 3:
                count += 1  
                
                
                print("jackpot",count)

   
