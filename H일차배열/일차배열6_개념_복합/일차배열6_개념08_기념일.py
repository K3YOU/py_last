'''
	[문제]	
		철수와 영희는 3월 3일에 만났다. 		
		철수는 영희와 100일 기념일에 축하 파티를 하려 한다.
		만난 지 100일 뒤는 몇 월 며칠인지 구하시오.
		단, 윤년은 계산하지 않으며, #2월 29일 금지
		시작일은 포함시키지 않는다.
	[정답]
		6월 11일
'''

monthList =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #달의 마지막 날짜

month = 3
day = 3

total = 0 

# 3월 3일 => 1월+2월+3일 :3월 3일을 만든 다음 거기서 100을 더하고 month랑 day로 분배
for i in range(len(monthList)):
	if i < month-1 :
		total += monthList[i]
	if i == month -1 :
		total += day
total += 100	
print("total :",total) #162 : 1.1 ~ 3.3

#month랑 day로 배분하는 법

##total - 3월3일까지의 일수

###total 
for i in range(len(monthList)):
	temp = total                        #바로 이전의 값을 꺼내고 싶을 때 임시 변수를 정한다
	total -= monthList[i]               #여기서 이미 빼주기때문에 0을 넘는지 안 넘는지는 뒤에 가서 안다.
	print(i,total)                     
	if total < 0 :                     #이 파트가 for바로 아래에 있으면 바래 아래 처럼 굳이 한 번 더 더해줄 필요 없을 듯??
		total += monthList[i]          #여기가 중요하다! -이면 100일 넘은 날이라 100일을 넘기게 한 달은 다시 더해준다.
		print((i+1),total)             #(i+1)의 이유는 배열이 0부터 시작하므로! 실제 달은 +1 
		break

print((i+1),"월",total,"일")




'''
3월 3일 전에 해당하는 달과 요일은 먼저 빼주고 더한 다음 100이 넘으면 멈추고 total을 백으로 만든 다음 month와 day로 배분-> 안 됌. total >= 100 으로 나오면 100으로 맞추주기가 힘듦
for i in range(len(monthList)-month+1):
	#month보다 작은 값은 다 배열에서 삭제
	if monthList[i] < month:
		monthList.remove[monthList[i]]
	#3월 중에서 day만큼은 빼주기
	elif monthList[i] == month:
		monthList[i] = monthList[i] - day
		total += monthList[i]
	else :
		if total < 100 :
			total += monthList[i]
		else :
			break

	
print(total)


total -= 20 #100

for i in range(len(monthList)):
	if monthList

'''



'''
total = 0 
for i in range(month - 1): 
	total += monthList[i] 
total += day #3/ 4
print("total =", total)

total += 100 
print("total =", total)

i = 0
while True:
	temp = total
	total -= monthList[i]
	if total < 0 :
		print((i+1), temp)
		break
	i += 1
'''


