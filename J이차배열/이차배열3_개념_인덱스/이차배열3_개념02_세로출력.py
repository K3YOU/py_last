'''
    [문제]
        a리스트를 각 세로별로 출력해보시오.
    [정답]
        [1] 0,0,3,1,4,2
        [2] 0,2,1,4,1,1
        [3] 0,0,3,2,4,4
        [4] 0,0,0,0,0,3
        [5] 3,3,1,2,4,3
'''

a = [
    [0,0,0,0,3],
    [0,2,0,0,3],
    [3,1,3,0,1],
    [1,4,2,0,2],
    [4,1,4,0,4],
    [2,1,4,3,3],   
]

for i in range(5):
    for j in range(6):
        print(a[j][i], end=" ") 
    print()