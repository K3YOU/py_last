'''
	[문제]
		a 리스트가 데칼코마니인지 구하시오.
		데칼로마니이면 True를 출력 아니면 False 출력하시오.
		데칼코마니란? 절반으로 나눴을 때 서로 값들이 대칭이면 데칼코마니이다.

	[예시]	
		[1,5,4,4,5,1] True
		[1,5,4,3,5,1] False
'''

#절반만 돌려서 푼 경우

a = [1,5,4,4,5,1]

middle = len(a) // 2  #6//2
 
count = 0

index = len(a) - 1 #5
for i in range(middle): #절반만 돌리는거지~
	if a[i] == a[index]: # a[0] == a[5], a[1]==a[4]
		count += 1 #count = 1,2
	index -= 1 #index = 4,3

if count == middle:  #count == 3
	print(True)
else:
	print(False)
	
