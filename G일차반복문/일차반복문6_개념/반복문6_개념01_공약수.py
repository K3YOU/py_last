'''
[문제]
	90과 45의 공약수를 출력하시오.
[정답]
	1 3 5 9 15 45
'''
i = 1
while i <= 45:
	if 90 % i == 0 and 45 % i == 0:
		print(i, end=" ")
	i += 1


