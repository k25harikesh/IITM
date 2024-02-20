T = int(input())

if T < 0 or T >= 24:
    print('INVALID')
elif T <= 5:
    print('NIGHT')
elif T <= 11:
    print('MORNING')
elif T <= 17:
    print('AFTERNOON')
elif T <= 23:
    print('EVENING')
