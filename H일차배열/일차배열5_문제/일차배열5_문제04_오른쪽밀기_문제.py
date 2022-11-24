'''
	[문제]
		a리스트의 값중 0을 제외하고 모든값을 오른쪽으로 모으시오.
 	[결과]
 		a = [0,0,0,0,0,0,2,3,4,5];
'''
import random

a = [0,0,2,0,3,0,4,0,0,5]



#오른쪽으로 모는 경우 : index = len(a)-1로 하고 , index -= 1
#오른쪽 밀기만 변수 2개 주는 이유 : for의 i는 왼쪽 0에서 시작해서 오른쪽 제일 큰 값의 방향으로 가지만, 이 경우 반대로 가야해서

j = len(a) - 1 #i 대신    #9
idx = len(a) - 1 #0을 넣을 곳 #9
for i in range(len(a)):
	if a[j] != 0: #a[9] = 5 
		temp = a[idx] #temp = a[9]
		a[idx] = a[j] #a[9] = 5
		a[j] = temp # a[9] =0 
		idx -= 1
	j -= 1
	

print(a)
