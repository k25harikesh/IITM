number = int(input())
maximumNumber = number

endOfInput = False
while not endOfInput:
    if number > maximumNumber:
        maximumNumber = number

    number = int(input())
    if number == 0:
        endOfInput = True

print(maximumNumber)
