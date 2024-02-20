def insert(L, x):
    sorted_lst = []
    L.append(x)
    while L:
        min = L[0]
        for i in L:
            if i < min:
                min = i
        sorted_lst.append(min)
        L.remove(min)
    return sorted_lst
