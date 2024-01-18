def get_average(marks):
    # total = 0
    # for i in marks:
    #     total += marks[i]
    # average = total / len(marks)

    average = sum(marks.values()) / len(marks)
    return average

marks = {'국어': 90, '영어': 80, '수학': 85}

average = get_average(marks)
print(f'평균은 {average}점입니다.')