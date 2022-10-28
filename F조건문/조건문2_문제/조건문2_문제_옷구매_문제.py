'''
	[문제] 
		철수는 상점에서 24600원짜리 옷을 구매했다.
		500원짜리 동전으로만 옷값을 낸다면,
		동전이 몇 개 필요한지 구하시오.
	[정답]
		50
'''
cloth = 24600
pay = 500

#pay_count = ?

if cloth % pay  != 0 :
	pay_count = (cloth//pay + 1)
	print(pay_count) 