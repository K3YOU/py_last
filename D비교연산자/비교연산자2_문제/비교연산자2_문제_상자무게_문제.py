'''
    [문제]
        무게가 2킬로그램인 상자에 한 개에 5킬로그램인 
        물건을 x개 넣으면 전체 무게가 30킬로그램을 넘는다.

        위 식을 표현하고, 풀이 과정을 주석으로 작성하시오.
'''
box = 2
obj = 5
max = 30
obj_count = (max-box) / obj 

print(max<= box + obj*obj_count)