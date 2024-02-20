def solution(marks):
    # Enter your solution below this line
    # Indent your entire code by one unit (4 spaces) to the right
    sorted_marks = []
    while marks:
        min = marks[0]
        for x in marks:
            if x < min:
                min = x
        sorted_marks.append(min)
        marks.remove(min)

    n = len(sorted_marks)

    median = sorted_marks[n // 2] if n % 2 == 1 else (
        sorted_marks[int(n / 2)] + sorted_marks[int(n / 2 - 1)]
    ) / 2
    # Enter your solution above this line
    return median


print(
    solution(
        [60, 10, 30, 40, 20, 50]
    )
)
