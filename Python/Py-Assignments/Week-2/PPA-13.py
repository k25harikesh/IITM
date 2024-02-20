runs_A_1 = int(input())
wickets_A_1 = int(input())

runs_A_2 = int(input())
wickets_A_2 = int(input())

runs_B_1 = int(input())
wickets_B_1 = int(input())

runs_B_2 = int(input())
wickets_B_2 = int(input())

if runs_A_1 + runs_A_2 > runs_B_1 + runs_B_2 and \
        wickets_B_2 == 10:
    print('Team A')

elif runs_B_1 + runs_B_2 > runs_A_1 + runs_A_2:
    print('Team B')

else:
    print('DRAW')
