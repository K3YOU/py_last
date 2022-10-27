'''
	[문제]
		현금이 10000원을 가지고,
		가격이 1200원인 과자 6개를 구입 후 거스름돈을 구하시오.
		단, 과자를 3개를 구입할 때마다 200원씩 할인해주는 행사를 진행 중이다. 
		
	[정답] 
		3200
'''

money = 10000
snack = 1200
snack_amo = 6

dis_snack_amo = 3
dis_snack_money = 200


'''
10000 - 1200*6 -200*(6 //3)


'''
change = money -snack*snack_amo + (snack_amo//dis_snack_amo)*dis_snack_money

print(change)


