"""
[문제]
    철수는 5440미터를 가는데 1시간 12분이 걸렸다. 
    철수의 시속은 얼마인지구하시오.
    소수점 두자리로 구하시오.
[정답]
    4.53
"""


분속 = 5440/ 72
시속 = 분속 * 60 * 1/1000

print("1 :", round(시속,2))


"""
[문제]
    철수는 시속3km의 속도로 2시간 21분을 걸었다.
    철수는 몇km를 걸었는지 구하시오.
    소수점 두자리로 구하시오.
[정답]
    7.05
"""
철수시속 =3
철수분속 = 3000
철수분간 = 141  #철수시간 = 2시간 21분

철수거리 = 철수분속 * 철수분간 * 1/60 * 1/1000

print("2 :", 철수거리)


"""
[문제]
    철수는 반장선거를 한다.
    전체인원 32명이다. 
    철수는 반장선거에서 7표를 받았다. 
    하였다. 몇퍼센트를 득표한것인지구하시오.
    소수점 두자리로 구하시오.
[정답]
    21.88
"""
전체인원 = 32
철수득표 = 7

퍼센트 = 철수득표/전체인원 * 100

print("3 :", round(퍼센트,2))