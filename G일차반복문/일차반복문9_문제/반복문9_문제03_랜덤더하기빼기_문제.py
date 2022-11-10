'''
	[문제]
		숫자 5개를 랜덤으로 뽑고, 
		랜덤으로 더하기나 빼기를 한 총합을 구하려고 한다.
  
		변수 r 은 숫자를 표현하며, 변수 op는 기호를 표현한다.
		변수 r 에 랜덤숫자(1~9)를 5개를 뽑는다. 
		또 op변수는 더하기나 빼기를 뜻하는 랜덤숫자(0, 1)도 4개를 뽑는다. 
		(기호는 숫자보다 1개 적어야 한다.)
		op 변수의 0은 더하기고 1은 빼기이다. 
		
		[예시]
			r 은 3, 6, 5, 3 , 1이 나왔다고 가정하고,
			op 는 0, 1, 0, 1이 나왔다고 하면, 
	
			3 + 6 - 5 + 3 - 1 이된다. 
'''

import random

#r =숫자를 5개 뽑기 #r의 개수를 세주는 변수도 필요
#op = 더하기 빼기 4개 뽑기 #op의 개수를 세주는 변수도 필요 
	 # r->op ->r ->op     sum
#sum =총합구하기

run = 1
count = 0
count1 = 0
sum = 0
while run == 1:
	r = random.randint(1,9)
	print(r, end = " ")
	count += 1
	if count == 5 and count1 == 4:
		run = 0
	
	else: #count가 5가 아닐 때랑 count1이 4가 아닐 때 부호를 한번 더 출력하기
		op = random.randint(0,1)
		count1 += 1
		
		if op == 0 :
				print("-",end = " ")
				sum -= r
		if op == 1:
				print("+",end= " ")
				sum += r
		

print()
print("sum",sum)

'''
print("##################################################################")



sum = 0
i = 0
while i <=4 :
	r= random.randint(1,9)
	print(r,end= " ")

	op = random.randint(0,1)
	if op == 0 :
		sum -= r
		print("-")
	if op == 1:
		sum += r
		print("+")
	
	
	i += 1
print("sum :" , sum) 

		

print()
print("sum",sum)
'''
