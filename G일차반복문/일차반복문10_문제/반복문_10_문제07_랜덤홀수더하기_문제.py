'''
	[문제]
		랜덤으로 2~5 를 저장하고, 
		랜덤숫자의 개수만큼 숫자를 더하는 문제와 답을 만들어 출력하시오..
		단 더하기 할 숫자들은 1~9사이의 홀수인 랜덤숫자여야 한다. 
		
		아래 [출력] 뒤에 나오는 모양과 똑같은 모양으로 출력한다. 
		(단, 숫자는 랜덤이므로 숫자는 다르게 나올 수 있다.)
			
		[예시1]		  		
			랜덤 ==> 3
			[출력] 5 + 3 + 1 = 9
			
		[예시2]
			랜덤 ==> 5
			[출력] 1 + 5 + 3 + 7 + 1 = 17
'''

import random

sum = 0
count = 0
a = random.randint(2,5)
print("random ==>",a)

run =1
while run== 1:
	if a % 2 != 0 :
		
		b = random.randint(1,9)
		if b % 2 != 0: 
			print(b , end="")
			sum += b
		
			count += 1
			if count < a:
				print(" + " , end=" ")
			
			if count == a :
				print("=",sum)		
				run = 0
					
		
	if a % 2 == 0 : 
		print("even =>done")
		run = 0

#2-5 사이의 랜덤 숫자에서 홀수가 나오면 더하기
#홀수이면 1-9사이 숫자로 더하기
