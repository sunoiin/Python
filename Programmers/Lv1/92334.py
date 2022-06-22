def solution(id_list, report, k):
    # 동일한 유저에 대한 신고는 1회로 처리 -> report 중복 제거 필요
    # k번 이상 신고된 유저는 정지, 신고한 유저에게 메일로 발송

    # 1. 유저의 신고받은 횟수, 메일받을 횟수 딕셔너리 초기화
    report_cnt = {id: 0 for id in id_list}
    mail_cnt = {id: 0 for id in id_list}

    # 2. 집합을 이용하여 중복 없는 report 생성
    report = set(report)

    # 3. 신고 받은 횟수를 딕셔너리에 저장
    for id in report:
        report_cnt[id.split()[1]] += 1

    # 4. 신고 받은 횟수가 k 이상이라면, blocked_id에 추가
    blocked_id = []
    for id, cnt in report_cnt.items():
        if cnt >= k:
            blocked_id.append(id)

    # 5. 신고 리스트에서, blocked_id를 신고한 사람이 메일 받는 횟수 추가
    for i in report:
        if i.split()[1] in blocked_id:
            mail_cnt[i.split()[0]] += 1

    answer = list(mail_cnt.values())

    return answer


print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2
))
# [2, 1, 1, 0]

print(solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
))
# [0, 0]
