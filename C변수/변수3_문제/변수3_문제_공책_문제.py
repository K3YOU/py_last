'''
	[문제]
		철수는 친구의 생일 선물로 가격이 4000원인 필통 1개와 
		가격이 700원인 공책 몇 권을 사려고 한다. 
		철수는 13000원을 가지고 있을 때,
		공책은 최대한 몇 권을 살 수 있을지 구하시오.
		공책을 최대로 구입한 후 나머지 금액도 출력하시오.
		
	[정답] 
		12
        600
'''

돈 = 13000 - 4000
공책 = 700
공책갯수 = 돈 // 공책
나머지금액 = 돈 % 공책

print(공책갯수)
print(나머지금액)