firstString = input()
secondString = input()

for char in firstString:
    secondString = secondString.replace(char, '')

print(secondString)
