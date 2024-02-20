'''

Accept two positive integers x and y as input. Print the number of digits in xy. You should be able to solve this problem using the concepts covered in week-1.

'''

a = input()
b = input()
fdgt = int(a) ** int(b)
# print(fdgt)
strfdgt = str(fdgt)
print(len(strfdgt))