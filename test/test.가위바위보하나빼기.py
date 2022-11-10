import random

#가위,가위로 내어도 상관없다
me = random.randint(1,3)
me2 = random.randint(1,3)
you = random.randint(1,3)
you2 = random.randint(1,3)
print("me :",me,"me2 :",me2)
print("you :",you,"you2 :",you2)

# 2 2
# 2 1    # 1 : 가위/ 2: 바위 / 3 : 보

run= 1
while run == 1:
     #두번째 랜덤을 만들기 # 0이면 내가 가진 처음꺼, 1이면 내가 가진 두번째꺼
    r = random.randint(0,1)  #나
    r1 = random.randint(0,1) #너
    print("r :",r,"r1 :",r1)
        
    if r == 0:
            me_final = me
    if r == 1:
            me_final= me2        
    if r1 == 0 :
            you_final =you
    if r1 == 1:
            you_final =you2 
      
    if me_final == you_final :
        print("tie")

    if me_final == 1 and you_final == 2:
        print("you win")     
    if me_final == 2 and you_final == 3:
        print("you win")    
    if me_final == 3 and you_final == 1:
        print("you win")    
 
    if me_final == 2 and you_final == 1:
        print("me win")    
    if me_final == 3 and you_final == 2:
        print("me win")    
    if me_final == 1 and you_final == 3:
        print("me win")   
    run = 0  