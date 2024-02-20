def is_empty(L):
    k = False
    if len(L) == 0:
        k = True
    return k


def first(L):
    if len(L) != 0:
        return L[0]
    else:
        return None


def last(L):
    if len(L) != 0:
        return L[-1]
    else:
        return None


def init(L):
    if len(L) != 0:
        L.remove(L[-1])
        return L
    else:
        return None


def rest(L):
    if len(L) != 0:
        L.remove(L[0])
        return L
    else:
        return None


L = [1, 3, 5, 32, 54]
print(rest(L))
