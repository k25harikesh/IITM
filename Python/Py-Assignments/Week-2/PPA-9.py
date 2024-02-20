coins = int(input())
share_1 = int(input())
share_2 = int(input())
share_3 = int(input())

if share_1 == share_2 or share_1 == share_3 or share_2 == share_3 or \
    share_1 == 0 or share_2 == 0 or share_3 == 0 or \
        share_1 + share_2 + share_3 != coins:
    print('UNFAIR')

else:
    print('FAIR')
