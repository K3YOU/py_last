'''
	[문제]	
		아래 리스트 a의 값을 사각형 모양으로 출력하시오.
	[예시]
		123
		456
		789
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#a의 개수가 몇개인지 정확히 숫자로 표현안해도 되는 이유 : 이미 a 배열 나와있으니깐..

count = 0
for i in range (len(a)):
	print(a[i],end=" ")
	
	if a[i] % 3 == 0 : #a[0]=1, a[3]=4, a[6]=7 #a[i]의 값이 순차적으로 1씩 커질 때 가능한 부분이다.
	# if i % 3 == 0 : 이면 a[i=0]에서의 i는 0 이므로 a[0]인 1이 혼자 첫줄에 나온다. 
		print()

		count += 1
		if count == 3:
			count = 0 #끝낸다는 의미

print()
print("====================")

run = 0
for i in range(len(a)): 
	print(a[i],end= " ")
	if i % 3 == 2: #앞에서 끊는게 아니라 뒤에서 끊는 방식
		print()
