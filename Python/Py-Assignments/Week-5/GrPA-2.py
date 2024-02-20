def is_perfect(n):
    lst = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    for i in lst:
        sum += i
    return (True if sum == n else False)
