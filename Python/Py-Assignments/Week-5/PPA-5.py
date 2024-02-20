def first_three(lst):
    sorted_lst = []
    while lst:
        min = float("inf")
        for i in lst:
            if i < min:
                min = i
        sorted_lst.append(min)
        lst.remove(min)
    return sorted_lst


lst = [1, 2, 7, 93, 87]
print(first_three(lst))
