'''
	[문제]
		a리스트에 랜덤(0 ~ 100) 사이의 랜덤 값을 4개 저장한 후 출력한다. 
		배열의 값은 학생들의 성적이다. 
		60점 이상이면 합격이다. 
  		전원합격 시 "상품" 을 출력. 
		전원탈락 시 "벌칙" 를 출력.
		그 외는 리스트만 출력하시오.
		
		[예시] 
			[67, 100, 98, 97] "상품"
			[53, 25, 12, 41] "벌칙"
'''
import random

a = []

#먼저 a를 채워넣고 시작 ->len(a)를 쓸 수 있다.
for i in range(4):
    r = random.randint(0, 100)
    a.append(r)
print(a)

c1 = 0 #passcount
c2 = 0 #failcount

#a를 pass랑 fail로 먼저 갈라두고 시작
for i in range(len(a)):
	if a[i] >= 60:
		c1 += 1
	if a[i] < 60 :
		c2 += 1

#pass와 fail 개수를 판별 아니면 리스트 출력
if c1 == len(a):
	print("상품")
elif c2 == len(a):
    print("벌칙")
else:
	print(a)
		



