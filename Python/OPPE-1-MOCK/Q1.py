num = input()

if not "l" or not "o" in num:
    print("No mistakes")
else:
    count = num.count('l')+num.count('o')
    if count != 0:
        print(f'{count} mistakes')
    else:
        print("No mistake")
    num = num.replace("l", "1")
    num = num.replace("o", "0")
    print(num)
