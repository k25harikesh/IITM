def get_range(lst):
    max = 0
    min = float('inf')
    for i in lst:
        if i > max:
            max = i
    for i in lst:
        if i < min:
            min = i
    return max-min
