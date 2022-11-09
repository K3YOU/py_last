'''
[문제]
	10000~99999 사이의 랜덤숫자를 저장하고 
	자리별숫자가 5 이상인 개수를 출력하시오.
	
		예) 19200 ==> 9 하나만 5 이상 ==> 1
		예) 98436 ==> 9,8,6, 세 개가 5 이상 ==> 3
'''

import random

a = random.randint(10000,99999)
print(a)


count = 0

run = 1
while run == 1:
	만 = a // 10000
	천 = a % 10000 // 1000
	백 = a % 10000 % 1000 // 100
	십 = a %10000% 1000 % 100 // 10
	일 = a % 10

	if 만 >= 5 :
		count +=1 
		if 천 >= 5 : 
			count = count +1
			if 백 >= 5 : 
				count = count +1
				
				if 십 >= 5:
					count =count +1 
					if 일 >= 5 : 
						count = count +1
						print(count)

						run = 0