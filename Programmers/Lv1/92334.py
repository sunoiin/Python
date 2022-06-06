def solution(id_list, report, k):
    answer = []
    blocked_id = []
    set_report = set(report)
    report_cnt = {id: 0 for id in id_list}
    mail_cnts = {id: 0 for id in id_list}

    for id in set_report:
        report_cnt[id.split()[1]] += 1

    for i in report_cnt:
        if report_cnt.get(i) >= k:
            blocked_id.append(i)

    for i in set_report:
        if i.split()[1] in blocked_id:
            mail_cnts[i.split()[0]] += 1

    answer = list(mail_cnts.values())
    print(answer)
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

solution(id_list, report, k)
