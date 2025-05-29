import time

def PackageBuild(w,n):

    # 이 함수는 가로 길이가 w이고 총 개수가 n 인
    # 택배의 2차원 배열을 반환하는 함수이다.
    #
    
    # x,y좌표와 소포의 번호가 포함된 택배라는 리스트를 만든다.

    # x,y좌표는 절대좌표이다.
    # number는 택배의 번호이므로 1부터 시작한다.
    x = y = 0
    number = 1
    package = [x,y,number]
    
    # 택배들이 저장될 빈 2차원 배열을 만든다.
    packages = []

    # 첫번째 택배를 빈 배열에 넣는다.
    packages.append(package)

    # 좌표를 규칙에 따라 늘린다.
    while True:
        
        # 높이가 짝수일때 진행방향은 오른쪽이다.
        if y%2 == 0:
            for j in range(1,w):
                x += 1
                number += 1
                package = [x,y,number]
                packages.append(package)
                if number == n:
                    break
            
        # 높이가 홀수일때 진행방향은 왼쪽이다.
        else:
            for k in range(1,w):
                x -= 1
                number += 1
                package = [x,y,number]
                packages.append(package)
                if number == n:
                    break
        if number == n:
            break
        y += 1
        number += 1
        package = [x,y,number]
        packages.append(package)
        if number == n:
            break

    return packages

def solution(n, w, num):
    
    answer = 0
    ## 목표 택배인 num의 y좌표와 num 택배의 맨 위에 있는
    ## 택배 top_num 택배의 y 좌표를 비교하여 그 차를 구한다.
    nowPb = PackageBuild(w,n)

    # num 택배의 정보를 추출한다.
    j = 0
    for j in nowPb:
        if j[2] == num:
            numPack = j
            break

    # num택배의x값을 추출한다.
    num_x = numPack[0]


    # 어차피 마지막에 걸러지는 녀석이 제일 큰 y값을 가진다.
    i = 0
    for i in nowPb:
        if i[0] == num_x:
            top_num = i
    # 그게 바로 top_num이 된다.


    # top_num의 y좌표와 numPack의 y좌표의 차를 구한다.
    # 이때 자신까지 포함해야 하므로 1을 더해준다.
    answer = top_num[1] - numPack[1] + 1
    

    return answer

