'''
	[문제]
		
        랜덤숫자(1~9)사이의 숫자를  여섯개를 출력하고 
        각 숫자를 더하거나 빼는 식을 만들어 출력하시오..
        랜덤숫자가 홀수이면 더하기를 하고,
        랜덤숫자가 짝수이면 빼기를 하시오.
        단, 마지막숫자는 영향이 없다. 

        5 7 6 2 3 1 이라고하면

        5는 홀수이므로 더하기
        7은 홀수이므로 더하기
        6은 짝수이므로 빼기
        2는 짝수이므로 빼기
        3은 홀수이므로 더하기
        1은 마지막이므로 영향이 없다. 

        5 + 7 + 6 - 2 - 3 + 1 이된다. 

'''
import random

op = 0  #부호 나타내는거
total = 0
i = 1
run = 1

#5 + 먼저 출력하고 +는 가지고만 들어가서 +7 이렇게 연산해야하는 방향을 알려주기, 그래야 마지막 숫자 1을 더할지 뺼지 알 수 있다.
    
a = random.randint(1,9)
print(a,end= " ") # 5
total += a

#부호 프린트 : 5 +
if a % 2 != 0 :
    op = 1 #+
    
else :
    op = 2 #-
    


while run == 1:
    if i <=5 :
        a = random.randint(1,9) #1. 7

        #앞에서 결정난 부호(5 + 에서 +) 그대로 들고 들어온 거!
        if op == 1:
            print("+",end= " ") #2. 5 +
            total += a   
        if op == 2:
            print("-",end= " ")
            total -= a  
    
        print(a,end= " ") #3. 5 + 7
        if a % 2 != 0 :
            op = 1 #+
            
        else :
            op = 2 #-
    
    if i == 5:
        print("=", total)
        
        run = 0      

    i += 1



        

        

