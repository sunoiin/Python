def solution(n):
    # [1] 문자열 n의 앞자리부터 answer에 추가하고, 뒤집어서 returnㄴ
    # answer = []
    # n = str(n)
    # for i in n:
    #     answer.append(int(i))
    # answer.reverse()

    # [2] List Comprehension 이용, 문자열 n을 뒤집은 배열에서 한자리씩 추가
    # answer = [int(i) for i in reversed(str(n))]

    # [3] Map 이용, 뒤집은 문자열 n에서 원소를 하나씩 꺼내 int형으로 변환하여 list 생성
    answer = list(map(int, reversed(str(n))))
    return answer
