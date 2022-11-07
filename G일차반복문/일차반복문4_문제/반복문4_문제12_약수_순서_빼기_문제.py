'''
	[문제] 
		100의 약수 중에서 
        5번째 약수에서 2번째 약수를 뺀 값을 구하시오.
	[정답]
		8
'''
num = 100
i = 1
count = 0
a=0
b=0

while num >= i :
	if num % i == 0 :
		count += 1

		if count == 2:
			a = i
			print(i)
		if count == 5:
			b = i
			print(i)
	i += 1

c = b-a 
print(c)				