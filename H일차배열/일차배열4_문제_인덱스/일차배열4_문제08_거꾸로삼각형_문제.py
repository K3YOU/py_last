'''
	  	[문제]
		 	아래 리스트를 아래와 같이 출력하시오.
		[결과]
			1234
			567
			89
			0
'''



a = [1,2,3,4,5,6,7,8,9,0]

count = 0
end = 4
for i in range(len(a)):
	
	#1234 따로 567 따로 생각하기
	print(a[i],end= " ")
	count += 1
	if count == end :
		count = 0
		end -= 1
		print()

