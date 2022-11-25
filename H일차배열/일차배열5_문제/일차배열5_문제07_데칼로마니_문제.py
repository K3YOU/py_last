'''
	[문제]
		a 리스트가 데칼코마니인지 구하시오.
		데칼로마니이면 True를 출력 아니면 False 출력하시오.
		데칼코마니란? 절반으로 나눴을 때 서로 값들이 대칭이면 데칼코마니이다.

	[예시]	
		[1,5,4,4,5,1] True
		[1,5,4,3,5,1] False
'''

#다 돌려서 푼 경우

a = [1,5,4,4,5,1]


#check = False
count = 0

for i in range(len(a)):
	
	if a[len(a)-1-i] == a[i] :  #여기서 a[0] == a[5] 에서 a[5] == a[0] 까지 다 돌림
		count += 1
		#check = True 
		
print(a,count)


if count == len(a) : #다 돌리니깐 a길이랑 같은것!
	print("a is True")
else :
	print("a is False")

'''
	temp = a[i]
	a[i] = a[len(a)-1]
	a[len(a)-1] = temp
	'''
