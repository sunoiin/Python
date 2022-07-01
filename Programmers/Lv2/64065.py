def solution(s):
    answer = []
    # string으로 주어진 tuple을 set(int형 원소) 변환하여 list 저장
    s_split = (s[2:-2].split('},{'))
    n_tuple = []
    for i in s_split:
        n_tuple.append(set(map(int, i.split(','))))
    # set 길이 오름차순으로 정렬
    n_tuple.sort(key=lambda x: len(x))

    # set 차집합하여 원소 하나씩 저장
    answer.append(list(n_tuple[0]))
    for i in range(len(n_tuple)-1):
        answer.append(list(n_tuple[i+1]-n_tuple[i]))

    # int형 list로 변환
    answer = [i[0] for i in answer]
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))  # [111, 20]
print(solution("{{123}}"))  # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]
