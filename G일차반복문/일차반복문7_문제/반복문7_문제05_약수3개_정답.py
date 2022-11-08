'''
	[문제]
		어떤 수를 1부터 자기 숫자까지 나눠서 나눠지는 수를 약수라고 한다. 
		랜덤으로 1~100을 저장 후, 
		약수가 3개이면 "정답"을 
		아니면 "오답"을 출력하시오.
'''

import random

num = random.randint(1, 100)
print(num)

count = 0

약수 = 1
while 약수 <= num:
	if num % 약수 == 0:
		print(약수, end=" ")
		count += 1
	약수 += 1

print()
if count == 3:
	print("정답")
if count != 3:
	print("오답")