'''
	[문제] 
		1000의 약수 중에서 200~800 사이 중에 
		일의자리가 0인 수만 출력하시오.
	[정답]
		200
		250
		500
'''




num = 1000

i = 1

while i <= num :
	if 200 <= i <= 800 :
		if num % i == 0 :
			if i % 10 == 0:
				print(i)			
	i += 1


