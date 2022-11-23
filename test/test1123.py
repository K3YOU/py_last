"""
[문제]
    아래 배열은 11~22까지 12개의 값이 저장된배열이다.
    아래배열을 세로3 가로4 즉 3행 4열로 출력한다. 
    그후, 랜덤으로 11~22사이의 값을 하나 저장후 그값이
    몇행 몇열인지 출력하시오. 행은 세로 열은 가로를 뜻한다. 
[예시]
        <0><1><2><3>
    <0> 11 12 13 14
    <1> 15 16 17 18
    <2> 19 20 21 22

    r = 20 => 3행 2열 
    r = 17 => 2행 3열 
"""

a = [11,12,13,14,
15,16,17,18,
19,20,21,22]

import random
r = random.randint(11,22)
print("r",r)

vertical = 0 #행
horizen = 0  #열
first = 11

for i in range(len(a)):
    if a[i] == r:
        print(a[i],"가로(열)",horizen,"세로(행)",vertical,end= "")
    
    a[i] = first 
    #print(a[i],end= " ")
    #print("가로",horizen,end= " ")
    #print("세로",vertical)
    first += 1 

    #가로를 4단위로 나누기

    if i % 4 ==3 :
        #print()
        horizen += 1

    #세로를 3 단위로 나누기

    share = 4
    if i % share == 0  :
        vertical = 0
    share += 1
    vertical += 1
    if vertical == 4:
        vertical = 0


        
  

        