'''
	[문제] 
		200의 약수 중에서 짝수 중 
		80에 가장 가까운 수를 구하시오.
		만약 약수 중에 80이 있을 경우, 80이 정답이다.
	[정답]
		100
'''

num = 200
i = 1
a = 0
b = 0

while num >= i :
	if num % i == 0 :
		if i % 2 ==0  and i <= 80 :
			a = i
			print(a)
		if i % 2 == 0 and i > 80 and b == 0  :
			b = i
			print(b)
	i += 1

a_result = 80 -a
b_result = b - 80

if a_result > b_result:
	print(b)
else : 
	print(a)	










