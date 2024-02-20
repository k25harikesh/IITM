word = input()
shortestWord = word

endOfInput = False
while not endOfInput:
    if len(word) < len(shortestWord):
        shortestWord = word

    word = input()
    if word == 'abcdefghijklmnopqrstuvwxyz':
        endOfInput = True

print(shortestWord)
