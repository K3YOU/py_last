'''
	[로또]	
		아래 lotto 리스트에 1~45숫자를 순차적으로 저장한다. 
		셔플후 그중 가장앞에서 6개를 출력한다. 
'''

lotto = []

#랜덤으로 넣지만 중복방지
'''
import random
for i in range(45):
	
	r1 =random.randint(1,45)
	if r1 == a
	lotto.append(r1)
print(lotto)
'''

# 순차적으로 넣고 셔플하기
num = 1
run = 1
while run == 1:
	lotto.append(num)
	num += 1
	if num == 46:
		run = 0
print(lotto)

import random



##셔플하기 
### index1,index2 = 로또의 배열을 돌릴 변수
for i in range(len(lotto)*100):
	index1 = random.randint(0,len(lotto)-1)
	index2 = random.randint(0,len(lotto)-1)
	temp = lotto[index1] #temp = index1
	lotto[index1] = lotto[index2] #index1 = index2
	lotto[index2]= temp #index2 = temp 

print(lotto)

