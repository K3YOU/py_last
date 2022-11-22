'''
	[문제]	
		아래 리스트 a의 값을 사각형 모양으로 출력하시오.
	[예시]
		123
		456
		789
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count =0
for i in range (len(a)):
	print(a[i],end= " ") #i =0,1,2/3,4,5
	if a[i] % 3 == 0 :
		print()
		#count += 1 #count = 1,2,3/1,2,3
		#if count == 3: #count=3
		#	count = 0 #count = 0
