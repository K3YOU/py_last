'''
	[문제] 
		a 리스트의 값을 비교해서,
		그중에 짝수는 b리스트에 추가한다.
		그중에 홀수는 a리스트에 추가하시오.
	[정답]   
		b = [ 2, 22 ]
 		c = [ 49, 51, 17 ]
'''

a = [49, 2, 51, 22, 17]
b = []
c = []

for i in range(len(a)):
	if a[i] % 2 == 0 :
		b.append(a[i])
	else:
		c.append(a[i])
print(b)
print(c)	
