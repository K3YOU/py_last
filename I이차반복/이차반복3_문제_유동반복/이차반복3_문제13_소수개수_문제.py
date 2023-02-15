'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수의 개수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19
		개수 = 8
'''
import random

#2/15 : for문으로 푼 방법

r= random.randint(2,100)
print("r =", r)

#필요한 변수
# r :범위
#i = 소수로 나올 수
#j = 몫

c =0  #진짜 개수를 세는 변수
for i in range(r+1) : #i = 0 ~ r --> 실질적으로 필요한 수 : i+2 ~ r # 2이상
	if i <= 1: 
		continue

	count = 0
	for j in range(i+1 ) :  # 0 ~ i-1 --> needs : 1 ~ i (only 1 and me)
		if j <= 0 :
			continue
		
		else :
			if (i % j == 0 ):
				count += 1

	if count == 2:   #count == 2이면 약수라는 것을 안다. -- > 약수의 개수를 세는 것과는 별개
		print(i,end= " ")
		c += 1
		#break 가 여기 있으면 안된다. : c = 2로 항상 고정되어서 나온다

print()
print("count :",c)



			






















# r= random.randint(2,100)
# print("r=", r)

# i = 1
# count = 0
# while i<=r :

# 	if r % i == 0 :
# 		print(i)
# 		count += 1
# 	i += 1
# print("count :",count,end= " ")


