'''
[문제]
	75의 약수 중에서 작은 수부터 큰 수를 출력했을 때, 
	다섯 번째 약수만 출력하시오.
[정답]
	25
'''
count = 0 #순서 출력해야하니깐 변수로 지정

i = 1
while i <= 75:  # 75의 약수
	if 75 % i == 0: # 75의 약수
		count += 1  #순서 출력해야하니깐

		if count == 5:  #위에 카운트 변수랑 같은 줄인거 유의! 카운트가 커지다가 5가 되면 멈춘다는 것을 뜻함
			print(i)
	i += 1


