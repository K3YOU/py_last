'''
	[문제]
		두 개의 변수 a, b에 숫자를 랜덤(1~9 사이의 숫자)으로 저장한다.
		두 변수 중 a 가 값이 더 크면 arr1 배열에 저장한다.

 		b의 값이 더 크면 arr2 배열에 저장한다. 
		앞에서부터 순차적으로 저장한다. 
		만약에 값이 같으면 둘 다 저장한다. 
		총 다섯 번을 반복하고 배열을 출력하시오.
		
		[예시]
            a = [4, 3, 8, 3, 7]
            b = [5, 4, 8, 9, 7]
            arr1 = [8, 7]
            arr2 = [5, 4, 8, 9, 7]
'''
import random

a = []
b = []

arr1 = []
arr2 = []

i = 0
while i < 5 :
	r1 = random.randint(1,9)
	r2 = random.randint(1,9)
	a.append(r1)
	b.append(r2)

	if a[i] > b[i] :
		arr1.append(r1)
	if a[i] < b[i] :
		arr2.append(r2)
	if a[i] == b[i] :
		arr1.append(r1)
		arr2.append(r2)
	i += 1
print("a",a,"b",b,"arr1",arr1,"arr2",arr2)






