'''
	[문제]
		item 리스트는 상품의 번호이다.
		price 리스트는 상품의 가격이다.
		item과 price는 한 세트이다.
  
		order는 오늘 주문이 들어온 상품의 인덱스 번호이다. 
		count는 order에서 주문한 상품들의 개수이다.
		order와 count는 한 세트이다. 
		오늘의 매출을 출력하시오.
  
		[예시]
  			order : 0은 상품 1001 을 의미하는 것이고, 
  			count : 3은 1001상품을 3개 구매한 것이 된다.
			즉, 매출에 1500원을 추가한다.
   
			위 식대로 남은 주문도 전부 계산하시오.
	[정답]
		44500
  
'''
item = [1001, 1002, 1003, 1004]   #상품번호
price =[500, 1200, 4300, 2300]    #상품의 가격

order = [0, 1, 3, 3, 2, 2, 1]    #오늘 주문이 들어온 상품의 인덱스 번호
count = [3, 2, 2, 1, 3, 4, 3]    #오더애서 주문한 상품들의 개수

sum = 0
sum1 = 0

#order =>pirce*count

for i in range(len(order)):
	#price[i] = price[order[i]]  #order=>price 
	
	#price *count = sum
	sum = price[order[i]] * count[i]
	sum1 += sum
print(sum1)


for i in range(len(order)):
	print(price[order[i]]*count[i])
	sum += price[order[i]]*count[i]
print(sum)
	


