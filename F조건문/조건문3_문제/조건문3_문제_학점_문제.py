'''
    [문제]
        0에서 100 사이의 랜덤 숫자를 시험 점수로 저장한다.
        시험점수에 해당하는 학점을 출력하시오.
        아래는 점수표이다.
        100~91 이면 A학점,
        90~81  이면 B학점,
        80 이하는 "재시험"
        
        단, 만점이거나, A 학점과 B 학점의 일의 자리가 8점 이상이면 + 기호를 추가하시오.
        [예] 
            100 => A+
            88 ==> B+
            82 ==> B
            23 ==> 재시험
'''

import random

a = random.randint(0,100)
print(a)

b = a % 10 

if a >=98 :
    print("a+")

if 91 <= a < 98 :
    print(a)

if 88<= a <= 90 :
    print("b+")

if 81 <= a <= 87 :
    print(b)

if a <= 80:
    print("재시험")

