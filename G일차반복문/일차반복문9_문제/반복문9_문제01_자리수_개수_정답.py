'''
[문제]
	10000~99999 사이의 랜덤숫자를 저장하고 
	자리별숫자가 5 이상인 개수를 출력하시오.
	
		예) 19200 ==> 9 하나만 5 이상 ==> 1
		예) 98436 ==> 9,8,6, 세 개가 5 이상 ==> 3
'''

import random

num = random.randint(10000, 99999)
print(num)

count = 0
while num != 0:

    unit = num % 10 #뒤에서부터 하나씩 분리하는 방법
    print("unit",unit, end=" ") #하니씩 분리하고 하나씩 결과로 뽑아내기

    if unit >= 5: 
        count += 1

    num //= 10   #제일 뒷 숫자 빼고 또 돌려야하므로 10으로 나눈 몫만 챙기기
print()
print("count : ",count)

