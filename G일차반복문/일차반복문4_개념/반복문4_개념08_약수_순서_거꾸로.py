'''
[문제]
	852의 약수 중에서 큰 수부터 작은 수를 거꾸로 출력했을 때,
	다섯 번째 약수만 출력하시오.
[정답]
	142
'''
count = 0

i = 852  #큰수부터 출력하니깐 첫 수를 제일 크게 두기
while i >= 1: #1까지만
	if 852 % i == 0: #약수출력
		count += 1 #순서출력

		if count == 5: #다섯 번째이면 그만
			print(i)

	i -= 1 # 작아지는 것이므로 마이너스

count = 0 
i = 852
while i >= 1:
	if 852 % i == 0 :
		count += 1

		if count == 5 :
			print(i)

	i -= 1		
