def solution(players, m, k):
    answer = 0
    
    # 서버들이 들어갈 빈 공간을 정의한다.
    servers = []
    
    # 서버를 정의한다. 서버 번호와 수명을 원소로 가진다.
    server_num = server_age = 0
    server = [server_num, server_age]
    
    #시간이 흐른다.
    time_global = 0
    for time_global in range(0,24):
        
        # 서버들의 나이를 한살씩 맥인다.
        i = 0
        for i in servers:
            i[1] += 1

        # 나이가 많은 서버를 죽인다.
        for i in servers[:]:
            
            if i[1] == k:
                servers.remove(i)
        
        # 증설돼야 할 서버 개수 n을 구한다.
        # 원래 있던 서버만큼 뺀다.
        n = players[time_global]//m - len(servers)
        
        # n만큼 새로운 서버들을 더한다.
        for _ in range(1,n+1):

            server = [server_num, 0]
            servers.append(server)
            answer += 1
            server_num += 1

    
    
    return answer