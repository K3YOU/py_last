'''
	[문제]
		어느 농장에는 토끼와 오리가 모두 35마리가 있다. 
		토끼와 오리의 다리의 수의 합이 96개일 때, 
		토끼와 오리는 각각 몇 마리 인지 주석으로 표현하시오.
	[정답]
		토끼 = 13
		오리 = 22
'''
'''
	토끼 = x
	오리 = y

	x + y = 35
	4x + 2y = 96
	4(35 - y) + 2y = 96
	140 - 4y + 2y = 96
	-2y = 96 - 140
	-2y = -44
	y = 22
	x = 13
'''

토끼_다리 = 4
오리_다리 = 2
전체_다리수 = 96

전체수 = 35
토끼 = 13
오리 = 22
print(토끼 + 오리 == 전체수 and 토끼_다리 * 토끼 + 오리_다리 * 오리 == 전체_다리수)
