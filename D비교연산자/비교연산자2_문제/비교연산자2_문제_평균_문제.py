'''
    [문제]
	    시험 점수(국어, 수학, 과학) 3개의 평균이 60점 이상이면 합격이다.
	    국어 는 45점이고 수학은 89점이다.	   
 	    철수는 과학 점수를 최소 몇 점 받아야하는지 구하시오.
		점수는 1점 단위이다.
   
      	위 식을 표현하고, 풀이 과정을 주석으로 작성하시오.
'''

kor = 45
math = 89
sc = 180-45-89 

print(sc)
'''
(45 + 89 + sc)/3  >= 60
45+89+sc >= 180
sc > 180-45-89 

'''

print((kor+math+sc)/3 >= 60)