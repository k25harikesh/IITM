n = int(input())

for i in range(2, n + 1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0 and i != 2:
            isPrime = False
            break
    if isPrime and n % i == 0:
        print(i)
