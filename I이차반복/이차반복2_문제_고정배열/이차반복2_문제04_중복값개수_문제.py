'''
	[문제]
        a리스트와 b리스트를 전체 비교하여 
        a리스트 안에도 있고 b리스트 안에도 있는 값은 c리스트에 저장하시오. 
        단, b리스트에 같은 값이 두 개 있는 값만 추가하시오.
    [정답]
        [7, 3]
'''

a = [1, 2, 7, 40, 3, 6]
b = [1, 2, 7, 3, 7, 6, 2, 2, 3]
c = []

for i in range(len(a)):
    count = 0
    for j in range(len(b)):
        if a[i] == b[j] :
           count += 1
    if count == 2:
            c.append(a[i])
            #print("i",i,"j",j,a[i])

print(c)
            
            
            # if count == 2:    : 2개 이상인 숫자들도 카운트가 멈추니깐 여기서 같이 출력되는 것
            #         c.append(a[i])

        # if count == 2:
        #     c.append(a[i])
        #     print("i",i,"j",j,a[i])
'''
            i 1 j 6 2    : 2가 2개 이상이지만, j가 6일 때 카운트가 2가 되어서 2가 뒤에 더 있음에도 출력됨
            i 2 j 4 7    : j가 4일 때 count =2라서 22번으로 내려오고 출력됨
            i 2 j 5 7    : j가 5일 때 a[i]랑 a[j]랑 같지는 않지만 이미 count =2라서 출력됨 (이하 동일)
            i 2 j 6 7
            i 2 j 7 7
            i 2 j 8 7    
            i 4 j 8 3
            [2, 7, 7, 7, 7, 7, 3]
            
            '''

   