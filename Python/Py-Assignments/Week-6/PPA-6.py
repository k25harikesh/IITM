def type_of_sequence(lst):
    k = 0
    for x in lst:
        if mysterious(x):
            k += 1
    if k < 2:
        return "mildly mysterious"
    elif k >= 2 and k < 5:
        return "moderately mysterious"
    elif k >= 5:
        return "most mysterious"
