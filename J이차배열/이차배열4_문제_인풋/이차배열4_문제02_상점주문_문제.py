'''
    [문제]
        info는 온라인 쇼핑몰 상품 정보이다.
        가로를 기준으로 상품번호와 가격이다.
        예를 들어 [1001,500]은 1001은 상품 번호이고 500은 상품 가격이다.
        
        order리스트는 오늘 주문 목록이다.
        예를들어 [1001,3]은 1001상품을 3개 주문한 것이다.
        
        count리스트에 오늘 판매한 상품별 개수와 총 금액을 저장 후 출력하시오.   
    [정답] 
        [1001, 8, 4000]
        [1002, 5, 13500]
        [1003, 1, 1200]
        [1004, 2, 1600]
        [1005, 5, 11000]   
'''
info = [
    [1001,500],
    [1002,2700],
    [1003,1200],
    [1004,800],
    [1005,2200]]

order = [
    [1001, 3],
    [1005, 5],
    [1003, 1],
    [1001, 4],
    [1004, 2],
    [1002, 3],
    [1001, 1],
    [1002, 2]]

count = [
    [1001,0,0],
    [1002,0,0],
    [1003,0,0],
    [1004,0,0],
    [1005,0,0]]
