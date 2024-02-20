string = input()

if len(string) % 2 == 0:
    string = string[0:-1] if string[-1] == '.' else string + '.'

mid = len(string) // 2
print(string[mid - 1: mid + 2])
