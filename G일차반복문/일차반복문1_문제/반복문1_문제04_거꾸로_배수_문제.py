'''
    [문제] 아래 조건을 만족하는 식을 작성하시오.  
        [조건1] 10~1까지 거꾸로 반복문을 실행한다.
        [조건2] 3의 배수일 때는 "안녕"을 출력한다.
        [조건3] 3의 배수가 아닐 때는 숫자를 출력한다. 
    [정답]
        10
        안녕
        8
        7
        안녕
        5
        4
        안녕
        2
        1
'''
#num 사용해서 푼 방법
i = 1
num = 10

while i <= 10 :
    if i % 3 == 0 :
        print("hello")

    if i % 3 != 0 :
        print(num)  
    num -= 1      
    i = i + 1

'''
i = 1
num = 4

while i <= 4:
    print(num)
    num -= 1
i += 1
    
        '''