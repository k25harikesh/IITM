def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        var = 1
        while (n>1):
            var *= n
            n -= 1
        return var