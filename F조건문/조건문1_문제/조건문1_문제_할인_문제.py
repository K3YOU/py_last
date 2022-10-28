'''
	[문제]
		철수는 볼펜을 10~30개를 구입해야 한다. 
		
		볼펜 하나의 가격은 1200원이다. 	
		볼펜은 20개 이상 구매 시 볼펜 한 개에 100원을 할인해주고 있다. 
			
		볼펜 수를 랜덤으로 저장하고,
		철수가 지급해야 하는 금액을 출력하시오.
		[예]
			볼펜 수 = 22
			지급 금액 = 22 * 1100 = 24200
'''


import random

pen = random.randint(10,30)
print(pen)

pen_price = 1200


if pen >= 20 :
	pen_price =1100
	print(pen * pen_price)

if pen < 20 :
	pen_price = 1200
	print(pen * pen_price)


'''
over 20 pen => per 1100
and total price is 1100 * 20



'''
'''
검산

c = (1~ 19 * 1200)
c = (20 ~ 30 * 1200)


'''
