def distance(w1, w2):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    dist = 0
    if len(w1) != len(w2):
        return -1
    for i in range(len(w1)):
        x = w1[i]
        y = w2[i]
        dist += abs(alp.index(x)-alp.index(y))
    return dist
