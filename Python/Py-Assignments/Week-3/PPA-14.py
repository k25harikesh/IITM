n1 = int(input())
n2 = int(input())

if n1 > n2:
    n2, n1 = n1, n2

isCoprime = True
for i in range(2, n1 + 1):
    if n1 % i == 0 and n2 % i == 0:
        isCoprime = False
        break

print('Coprime' if isCoprime else 'Not Coprime')
