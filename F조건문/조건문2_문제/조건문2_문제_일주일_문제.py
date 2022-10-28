'''
	[문제]
		이번 달 1일이 수요일이라고 할 때, 
		랜덤으로 1~31을 저장하고 해당 요일을 출력하시오.

		[예]
		3일 ==> 금요일
'''


import random

month = random.randint(1,31)
print(month)
day = month % 7

'''
mon = 1
tue = 2
...
'''




if day == 1:
	print("wed")

if day == 2:
	print("thur")

if day == 3:
	print("fri")

if day == 4:
	print("sat")

if day == 5:
	print("sun")

if day == 6:
	print("mon")

if day == 0:
	print("tue")

