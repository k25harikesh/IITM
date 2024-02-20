n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if n1 > n2:
    n2, n1 = n1, n2

if n2 > n3:
    n3, n2 = n2, n3

if n1 > n2:
    n2, n1 = n1, n2

if n3 > n4:
    n4, n3 = n3, n4

if n2 > n3:
    n3, n2 = n2, n3

if n1 > n2:
    n2, n1 = n1, n2

print(n1, n2, n3, n4)
