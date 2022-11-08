"""
    [문제]
        아래 조건에 모두 맞는 결과를 출력하시오.
        [1] 랜덤 숫자 10개를 출력한다.
        [2] 랜덤 숫자는 2 또는 5만출력한다.
        [3] 단, 둘중하나라도 3개에 먼저도달하면, 남은개수는 반대편 숫자로 전부 출력한다. 

    [예시]
        2, 5, 5, 2, 5, 2, 2, 2, 2, 2  
    [예시]
        5, 5, 2, 2, 2, 5, 5, 5, 5, 5
"""
import random
a = random.randint(0,1)
print(a)

count = 0 #2의 개수
count1 = 0 #5의 개수
sum = count + count1

while sum<= 10 :
    if a == 0 :
        print(2, end = " ")
        count += 1
        
    if a == 1 :
        print(5, end = " ")
        count1 += 1

        if count




    
 




