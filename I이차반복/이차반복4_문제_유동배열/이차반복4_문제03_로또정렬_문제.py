'''
	[문제] 
		1~45사이의 랜덤값 6개를 lotto에 저장하려 한다.
		단, 중복되는 숫자는 없어야 하며,
		내림차순 정렬 후 출력하시오.
	[예시]
        [40, 38, 27, 26, 18, 5]
'''
lotto = []

import random

#중복없이 넣기

i = 0
while i<6 :
	r = random.randint(1,45)

	check = False 
	j = 0

	#중복이면
	while j<i :
		if r == lotto[j]:
	#사실이다
			check == True
	#사실이면 빠져나오기
			break
		j += 1

	#거짓이면
	if check == False:
	#다르다(추가)
		lotto.append(r)
		i += 1
print(lotto)

#큰수부터 정렬하기
i = 0
while i <len(lotto):
	max = lotto[i]
	maxindex = i

	j = i
	while j < len(lotto) :  # 1:n
		if max <lotto[j]:
			max = lotto[j]
			maxindex = j
		j += 1

	temp = lotto[i]
	lotto[i] = lotto[maxindex]
	lotto[maxindex] = temp
	
	i += 1
print("내림차순정렬")
print(lotto)





	



	#for문 쓰면 안된다. ->최대값만 계속 나옴 -> 이미 나온 최대값은 제외시키고 다시 최대값을 뽑는 것에 위배된다.
	# for i in range(len(lotto)):
	# 	max = lotto[i]
	# 	maxindex = i
	# 	for j in range(len(lotto)):
	# 		if lotto[i] <lotto[j] :
	# 			max = lotto[j]
	# 			maxindex = j
	# 	temp = lotto[i]
	# 	lotto[i] = lotto[maxindex]
	# 	lotto[maxindex] = lotto[i]
	# print("dfaf",lotto)		

	#while을 써야한다.














# i = 0
# while i <len(lotto):
# 	print(i,lotto)

# 	max = lotto[i]
# 	maxindex = i

# 	#나 다음부터 끝까지 
# 	j = i
# 	while j < len(lotto):
# 		if (lotto[j]>max):
# 			max = lotto[j]
# 			maxindex = j
# 		j += 1
	
# 	#값 바꾸기 (나를 제일 큰 수로 넣기)
# 	temp = lotto[i]
# 	lotto[i] = lotto[maxindex]
# 	lotto[maxindex] = temp
# 	i += 1 #그리고 제외하기

#print(lotto)

