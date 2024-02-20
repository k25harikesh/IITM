# n = int(input())

# isPrime = True
# for i in range(2, n):
#     if n % i == 0 or n == 2:
#         isPrime = False

# print('PRIME' if isPrime else 'NOTPRIME')

n = int(input())

isprime = True
for i in range(3, n):
    if n % i == 0 or n == 2:
        isprime = False
print('PRIME' if isprime else 'NOTPRIME')
