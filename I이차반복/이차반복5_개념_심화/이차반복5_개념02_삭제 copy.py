'''
	[문제]
		a리스트안에는 1~5의 값이 추가되어 있다. 
		랜덤(1~10) 숫자를 10번 발생시켜
		랜덤 값이 a리스트안에 있으면 a리스트에서 삭제하고,
		없으면 "삭제불가" 를 출력한다.
	[예시] 
		r = 9 : 삭제불가
		r = 9 : 삭제불가
		r = 8 : 삭제불가
		r = 3 : [1, 2, 4, 5]
		r = 6 : 삭제불가
		r = 6 : 삭제불가
		r = 8 : 삭제불가
		r = 5 : [1, 2, 4]
		r = 1 : [2, 4]
		r = 6 : 삭제불가
'''
import random

a = [1,2,3,4,5]

for i in range(10):
	r = random.randint(1,10)
	print("r=",r,":",a)

	count = 0
	index = 0
	for j in range(len(a)): #len(a)의 길이를 줄여야함
		if a[j] == r:
			index = j
			break
		else:
			count += 1
	if count != len(a) :
		del a[index]
		print(a)
	else :
		print("can't delete")


		
