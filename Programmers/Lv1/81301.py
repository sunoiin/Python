def solution(s):
    answer = s

    nums = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']

    for num in nums:
        if num in answer:
            answer = answer.replace(num, str(nums.index(num)))

#     num_dic={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)

    return int(answer)
