'''
    [문자열 리스트]
        [1] 문자열도 숫자와 마찬가지로 리스트로 만들 수 있다. 
            a = ["김철수", "이민수", "유영희"]
            
        [2] 리스트는 숫자와 문자를 섞어서 만들 수 있다.
            b = [1001, "김철수", 1002, "이민수", 1003, "유영희"]
            
        [3] 이차원 리스트도 만들 수 있다.
            c = [
                    [1001, "김철수"],
                    [1002, "이민수"],
                    [1003, "유영희"]
                ]
'''
a1 = [1001, 1002, 1003]
a2 = ["김철수", "이민수", "유영희"]
print(a1)
print(a2)
print("---------------------------------------------------------")
b = [1001, "김철수", 1002, "이민수", 1003, "유영희"]
print(b)
print("---------------------------------------------------------")
c = [
        [1001, "김철수"],
        [1002, "이민수"],
        [1003, "유영희"]
    ]
for i in range(len(c)):
    print(c[i])