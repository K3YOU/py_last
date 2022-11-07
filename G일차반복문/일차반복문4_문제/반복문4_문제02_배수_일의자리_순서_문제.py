'''
	[문제] 
		9의 배수 중 일의 자리가 6인 
		첫 번째 배수를 출력하시오.
	[정답]
 		36
'''

#count 안 써도 된다. 
i = 1
run = 1
while run == 1 :
	if i % 9 == 0 :
		if i % 10 == 6 :
	
			run = 0
			print(i, end = " ")
	i += 1		