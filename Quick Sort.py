n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개일 경우 종료
        return
    pivot = start  # 첫 번째 원소를 pivot으로 설정
    left = start+1
    right = end

    # 왼쪽에서부터 pivot보다 큰 값 선택, 오른쪽에서부터 pivot보다 작은 값 선택
    while (left <= right):
        # left 값이 pivot보다 클 때 까지 left 1씩 증가
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # right 값이 pivot보다 작을 때 까지 right 1씩 감소
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        # 만약 left 인덱스가 right보다 크면 (엇갈리면) 작은 데이터(right)와 pivot 값 swap
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        # left보다 right 인덱스가 크면, 서로 swap
        else:
            array[left], array[right] = array[right], array[left]

    # array를 분할하여 다시 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, n-1)

for i in array:
    print(i)
