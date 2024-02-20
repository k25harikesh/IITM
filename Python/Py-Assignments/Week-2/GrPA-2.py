E1 = int(input())
E2 = int(input())
E3 = int(input())
E4 = int(input())
E5 = int(input())

if (E1 % 2 == 0 and E2 % 2 == 0 and E3 % 2 == 0 and E4 % 2 == 0 and E5 % 2 == 0) or \
        (E1 % 2 == 1 and E2 % 2 == 1 and E3 % 2 == 1 and E4 % 2 == 1 and E5 % 2 == 1):
    print('YES')

else:
    print('NO')
