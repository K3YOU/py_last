'''	
 [문제] 
    아래 변수의 a의 값이 
    100의 자리가 45의 약수이면, True를 출력하시오.
'''
a = 3640

print(45 % (a % 1000 // 100) == 0)