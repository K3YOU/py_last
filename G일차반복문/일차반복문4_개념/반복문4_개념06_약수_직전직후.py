'''
[문제] 
    280의 약수 중에
    50바로 전의 값과 바로 뒤의 값을 구하시오.
    만약 50이 약수이면, 바로 뒤의 값은 50이다.
[정답]
    40
    56
'''

front = 0
back = 0

i = 1
while i <= 280: 
    print(i)
    if 280 % i == 0: #280의 약수 중에  
        if i < 50: # 50보다 작으면
            front = i #i는 front가 된다
        if i >= 50 and back == 0: #50보다 크면서 50이상일 때 최초의 값을 표현한 것 => back ==0
            back = i #i는 back이 된다.
    i += 1  #위 조건들이 나올 때 까지 반복한다는 의미.


print(front)
print(back)



