"""
[문제]
    어떤사각형의 가로와 세로를 구하고싶다.
    다음 조건에 맞는 사각형 구하는 식을 적으시오.
    최소 길이는 1m 이며 , 1m단위로 계산한다. 
    [1] 사각형의 넓이는 24m이다.
    [2] 사각형의 가로는 세로보다 길다.
    [3] 사각형의 가로길이는 세로길이보다 2배는 넘는다. 
    [4] 사각형의 가로길이는 세로길이보다 3배는 넘지않는다.

"""
"""
가로 * 세로 = 24
3*세로>가로 > 2*세로

"""


print("1번문제")
garo = 1 #garo

while garo<= 24 :
    sero = 24// garo 
    if garo * sero  == 24 and 3*sero > garo > 2* sero :
        print("garo",garo,"sero",sero)
    garo  += 1


print()

"""
[문제]
    중학생인 미연이는 부모님과 함께 미술관에 갔다.
    어른의 입장료가 청소년의 입장료보다 2,000원이 더 비싸고,
    세 사람의 입장료가 13,000원일때, 미연이의 입장료를 구하시오.
[정답]
    미연
"""
'''
어른 : x : 5000
청소년 : y : 3000
x = y + 2000
2x +y = 13000
y = 13000 - 2x
2(y + 2000) + y = 13000
3y + 4000 = 13000
3y = 9000
y = 3000 
'''
print("2번문제")
adult = 0
run = 1
while run == 1:
    kid = adult - 2000 

    if adult == kid + 2000 and kid == 13000 - 2*adult and adult >= 2000:
        print(kid,"원")
        run = 0
    adult += 1    

print()
'''
	[문제]
		아래 배열은 3명의 학생 데이터이다.		
		각 학생은 3개씩 데이터로 표현한다. 
		맨 앞은 번호, 그다음은 국어점수, 그다음은 수학점수이다.					
		(예) 
			1001번, 국어 100, 수학 20
			1002번, 국어 32,  수학 54
			1003번  국어 34,  수학 65	

		
		[4] 전체 1등 학생을 출력하시오.
'''

a = [1001, 100, 20, 1002, 32, 54, 1003, 34, 65]
#    0       1   2   3     4   5   6    7    8

sum = 0
kor = 0
math = 0
 



'''
sum = 0
print("3번문제")
for i in range(len(a)):
    if i % 3 == 0 :
        print(a[i],"번",end= " ")
        
    if i % 3 == 1 :
        print("국어",a[i],end= " ")
       
    if i % 3 == 2 :
        print("수학",a[i])
print()
'''
'''      
for i in range(len(a)):
    if i % 3 == 0 :
        sum += a[i+1] 
        sum += a[i+2] 
        print(i,sum)
'''


  
        
      






    





