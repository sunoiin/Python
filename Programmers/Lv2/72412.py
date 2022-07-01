def solution(info, query):
    answer = []
    # 처음부터 set으로 만들면..?
    info = [set(i.split()) for i in info]
    query = [i.split(' and ')[:-1] + i.split(' and ')[-1].split()
             for i in query]
    bar = set('-')
    # print('info', *info, sep='\n')
    # print('query', *query, sep='\n')

    # # query <= 100,000 info <= 50,000
    for i in range(len(query)):
        set_query = set(query[i])
        score = int(query[i][-1])
        cnt = 0
        # print(query[i])
        for j in range(len(info)):
            tmp = set_query-info[j]-bar
            if len(tmp) == 0:
                cnt += 1
            elif len(tmp) == 1 and list(tmp)[0].isdigit:
                for k in info[j]:
                    if k.isdigit() and int(k) >= score:
                        # print(info[j], k, score)
                        cnt += 1
        answer.append(cnt)

    return answer


print(solution(
    ["java backend junior pizza 150",
     "python frontend senior chicken 210",
     "python frontend senior chicken 150",
     "cpp backend senior pizza 260",
     "java backend junior chicken 80",
     "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100",
     "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250",
     "- and backend and senior and - 150",
     "- and - and - and chicken 100",
     "- and - and - and - 150"]))
