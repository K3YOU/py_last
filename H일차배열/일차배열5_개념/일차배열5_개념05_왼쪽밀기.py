'''
	[문제]
		a리스트의 값 중 0을 제외한 모든 값을 왼쪽으로 모으시오.
 	[결과]
 		a = [2,3,4,5,0,0,0,0,0,0];
'''


a = [0,0,2,0,3,0,4,0,0,5]

index  = 0
for i in range(len(a)):
	if a[i] != 0:  #요소가 0이 아닌 경우
		a[index] = a[i] #0부터 시작하는 인덱스(=왼쪽에서 시작)에 값을 넣어준다
		a[i] = 0 #원래 값은 0으로 바꾼다

		index += 1 #index는 1씩 커진다 -> 왼쪽에서 0으로 채워지게

print(a)




#오른쪽으로 모는 경우 : index = len(a)-1로 하고 , index -= 1