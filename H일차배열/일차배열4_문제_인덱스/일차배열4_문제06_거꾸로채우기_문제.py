'''
	[문제]
		공간이 10개인 a리스트가 있다. 
		랜덤(0~9)로 시작 인덱스를 저장한다.
		랜덤(1~10)로 개수를 저장한다.
		시작 인덱스부터 개수만큼 거꾸로 숫자를 채워나간다.
		채우는 숫자는 1부터 1씩 증가한다.
		
	[예시]
		ranIndex = 3 
		ranCount = 7		
  		a = [4,3,2,1,0,0,0,7,6,5]  
  			- 인덱스 3부터 7개를 채운다. 
	

'''
##번외문제!!

a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] #-1로 채워진 배열을 위와 같은 a로 바꾸어라  ->append가 아니라 기존의 것을 채워넣는 방식으로 해야한다.

import random
'''
ranindex = random.randint(0,9) #시작점
rancount = random.randint(1,10) #숫자몇개넣을지

print(ranindex,rancount)
'''
ranindex = 7
rancount =8

count = 1

for i in range(len(a)):
	a[ranindex] = count
	#a.append(a[ranindex])

	ranindex -= 1
	count += 1
	#if count == ranindex :
	#	count = 0
	if i >= rancount-1: 
		count = 0
	

	if ranindex <0 :
		ranindex = len(a) -1  #뒤에서부터 채워준다
		
print(a)

	

