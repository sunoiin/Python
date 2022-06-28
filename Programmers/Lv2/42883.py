def solution(number, k):
    stack = []
    for num in number:

        # stack에 원소가 있고, 마지막 원소가 현재 원소보다 작고, k가 남아있을 때
        while stack and stack[-1] < num and k > 0:

            # stack의 마지막 원소를 제거한다.
            stack.pop()
            k -= 1

        # stack에 현재 원소를 추가한다.
        stack.append(num)

    if k != 0:  # 동일한 숫자로 이루어져 있거나, 내림차순 정렬되어 있어 제거한 원소가 없는 경우, 앞에서부터 끊어서 출력
        stack = stack[:-k]

    answer = ''.join(stack)

    return answer
