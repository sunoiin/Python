# n: 부가서비스 수
# plans: 요금제 정보
# clients: 이용하려는 고객 정보 (데이터, 이용 부가서비스)

def solution(n, plans, clients):
    answer = [0 for i in range(len(clients))]
    # 고객마다 이용하려는 데이터 이상, 이용하려는 부가서비스 모두 포함하는 가장 싼 요금제
    # 조건 만족하는 요금제 없을 경우 0

    for i in range(len(plans)):
        plans[i] = list(map(int, plans[i].split(" ")))

    for i in range(len(clients)):
        clients[i] = list(map(int, clients[i].split(" ")))

    for i in range(1, len(plans)):
        plans[i] += (plans[i-1][1:])
    print(plans)

    for i in range(len(clients)):
        plan = clients[i][0]
        service = set(clients[i][1:])
        # print(plan, service)

        for j in range(len(plans)):
            if plans[j][0] < plan:
                continue
            if service.issubset(set(plans[j][1:])):
                print(j, service, set(plans[j][1:]))
                answer[i] = j+1
                print(j+1, "만족")
                break
    print(answer)

    return answer


solution(5, ["100 1 3", "500 4", "2000 5"], [
         "300 3 5", "1500 1", "100 1 3", "50 1 2"])  # 3 3 1 0
# solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"])  # 1 2 0
