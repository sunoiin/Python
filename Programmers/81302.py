def solution(places):
    answer = []

    for place in places:
        print(f'--{places.index(place) + 1}--')
        print(*place, sep='\n')

        distancing = 1

        for i in range(5):
            for j in range(5):

                # 1) 자기 원소가 P일 때, 상하좌우 원소에 P가 없다.
                if place[i][j] == 'P':
                    if i > 1 and place[i-1][j] == 'P':
                        distancing = 0
                        break
                    if j > 1 and place[i][j-1] == 'P':
                        distancing = 0
                        break
                    if i < 4 and place[i+1][j] == 'P':
                        distancing = 0
                        break
                    if j < 4 and place[i][j+1] == 'P':
                        distancing = 0
                        break

                # 2) 자기 원소가 O일 때, 상하좌우 원소에 P가 1개 이하이다.
                p_cnt = 0
                if place[i][j] == 'O':
                    if i > 1 and place[i-1][j] == 'P':
                        p_cnt += 1
                    if j > 1 and place[i][j-1] == 'P':
                        p_cnt += 1
                    if i < 4 and place[i+1][j] == 'P':
                        p_cnt += 1
                    if j < 4 and place[i][j+1] == 'P':
                        p_cnt += 1

                    if p_cnt > 1:
                        distancing = 0
                        break

        answer.append(distancing)

    return answer


print('answer:',
      solution([
          ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
      ]))
