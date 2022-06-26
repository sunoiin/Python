def solution(genres, plays):
    answer = []

    # 각 곡의 고유번호
    uniq_num = [i for i in range(len(genres))]

    # 장르별 재생횟수 합계를 딕셔너리, 내림차순 정렬
    best_genre = {}
    for genre, play in zip(genres, plays):
        if genre not in best_genre:
            best_genre[genre] = play
        else:
            best_genre[genre] += play
    best_genre = sorted(best_genre.items(), key=lambda x: -x[1])

    # 3. 장르 내에서 재생 횟수가 같은 노래 중 고유번호가 낮은 노래를 먼저 수록
    # -> 고유번호를 먼저 zip해주고, genre 오름차순, play 내림차순으로 정렬했기 때문에 자동으로 조건 만족
    genre_play_order = sorted(
        list(zip(genres, plays, uniq_num)), key=lambda x: (x[0], -x[1]))

    # 배열을 장르 기준으로 미리 정렬해놨고, 최대 연산 갯수가 2개이기 때문에 효율성이 크게 떨어지지는 않을 듯 함.
    # (장르 최대 100개 * 2번 연산 = 200번)
    for i in best_genre:
        cnt = 0
        for genre, play, order in genre_play_order:  # NOTE: play는 실제로 쓰이지 않는데, 리스트 전체를 for문으로 받아서 index로 접근하는게 더 효율적일까?
            print(genre, play, order)
            if genre == i[0]:
                cnt += 1
                answer.append(order)

            # 장르에 속한 곡이 하나일 경우: for문이 다음 장르로 넘어가기 때문에 별도 처리 필요 없음
            if cnt == 2:
                break

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],
      [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
