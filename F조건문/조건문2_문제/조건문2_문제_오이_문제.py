'''
	[문제]	  	
		마트에서 오이를 3개씩 묶어서 1500원에 판매한다.
		오이가 14개 필요하다면,
		필요한 금액을 출력하시오.
		단, 오이는 묶음으로만 판매한다.
	[정답]
		7500
'''

cu_basic = 3
cu_price = 1500

want_count = 14

#want_price = ?

if want_count % 3 != 0:
	want_price =1500*((want_count//3)+1)
	print(want_count,want_price)