"""
[문제]
    철수는 시속3km 로 5km를 갔다.  
    철수는 1시간 35분 보다 더걸렷으면 true 출력 
     # 시간비교문제 - 분끼리 비교
 
"""
["철수"]
거리 : 5
시간 : 3
속력 :5/3
분간 : 3/60
분속력 = 5/(3/60) 

print(분속력)

ㅁ = 95/60
ㅍ = 5/3


print(ㅍ , ㅁ)



"""
[문제]
    철수는 편의점에서 아르바이트를 하고있다. 

    손님이 현금으로 결제를 하고 거스름돈이 28000원이 나왔다. 
    지금 편의점에 잔돈중 1천원권 화폐가 전부 소진되었을때 
    철수는 각 화폐별로 몇장씩 나눠주어야하는지 작성하시오.

[예시]
    일만원 : 2장
    오천원 : 1장
    일천원 : 0장
    오백원 : 6개
"""

거스름돈 = 28000
만원권 = 거스름돈 // 10000  #2장
오천원권 = (거스름돈 % 10000) // 5000 # 1장
오백원권 =(거스름돈 % 10000) % 5000 //500

print("2번 정답 " , 만원권, 오천원권, 오백원권)


"""
[문제]
    오늘은 우유상점 매출 결과이다.
    오전에는 전체우유의 20 퍼센트를 팔았다. 
    오후에는 42개를 팔았다.

    남은우유는 오늘 전체우유의 73퍼센트이다. 
    오늘 전체 우유수는 몇개인지구하시오. 
"""

오전퍼센트 = 20 / 100
남은우유퍼센트 = 73/100 

오후 = 42
오후퍼센트 = 7 / 100 


#전체 = 오전 + 42 + 남은우유 

'''
42 : 7/100 = n : 1
7/100*n = 42
7n = 4200
n = 600

'''
전체우유 = 600
print("3번 정답 " ,전체우유)





"""
[문제]
    주차요금이 10500원이 나왔다. 몇분을 주차한것인가?
    <주차요금>
    기본 1시간 요금 : 3000원 (기본요금은 처음 한번만 적용된다)
    기본 1시간을 초과시 5분마다 500원씩 추가 
[정답]
    135
"""
기본요금 = 3000
추가요금 = 500
주차요금 = 10500
나머지시간 = 주차요금 - 기본요금
나머지세트 = 나머지시간 / 추가요금

전체시간 = 60 + 15 * 5

"""
135 - 60 = 75
10500 - 3000 => 7500 = 500 * 15
"""

print("4번 정답", 전체시간 )
"""
[문제]
    철수는 3분17초 동안 1000m를 달렸다. 
    영희는 4분28초 동안 1000m를 달렸다. 
    둘다 1400m를 달렸을때 철수가 영희보다 몇초가 빠른지 출력하시오. 
    단, 두사람은 항상 일정한속도로 달린다. 
    소수점 두자리로 출력하시오.
"""

철수속도 = 1000 / (3*60 + 17)
영희속도 = 1000 / (4 *60 + 28)

철수시간 = 1400 / 철수속도
영희시간 = 1400 / 영희속도

print("5번 정답 ", round(철수시간 - 영희시간, 2))

#print(round(영희시간 - 철수시간, 2))
#정답 : 99.4초

