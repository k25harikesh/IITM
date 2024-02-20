#L2 intro to loops

# year = int(input())

# while(year != 1947) :
#     print("you did a wrong guess, take one more chance !")
#     year = int(input())
# # else:
# print("hurrah you got it right")

# L3 Factorial

# n = int(input())
# i = 1
# ans = 1 

# while(i <= n):
#     ans *= i
#     i += 1
# print(ans)

# L4 Tutorial on while loop

# 4.1 another way to do factorial

# n = int(input("Enter a number : " ))
# if (n < 0):
#     print('not defined')
# else:
#     fact = 1
#     while(n > 0):
#         fact *= n
#         n -= 1
#     print(fact)

# Problem 4.2 (Find the numbers of digit in givven num)

# num = abs(int(input("Enter a num :" )))
# digits = 1
# while(num > 9):
#     num = num // 10
#     digits += 1
# print(digits)

# Problem 4.3 (find reverse of a number) (incomplete without negative numbers)

# n = int(input("Enter a num : "))
# rev = n % 10
# n = n // 10
# while(n>9):
#     rev = rev * 10 + (n % 10)
#     n = n // 10
# print(rev*10 + n)

# Problem 4.4 (find whether a num is palindrom or not)

# n = int(input("Enter a num : "))
# absn = abs(n)
# rev = absn % 10
# absn = absn // 10
# while(absn>0):
#     rev = rev * 10 + (absn % 10)
#     absn = absn // 10
# if n>=0 :
#     print(rev, "65") 
#     if n == rev :
#         print("palindrom")
#     else :
#         print('not a palinfrom')
# else :
#     print(-rev, "71")
#     if n == -rev :
#         print("palindrom")
#     else :
#         print('not a palindrom')


# L5 (Intro to for loop)
# L6 (adding n int)

# n = int(input('Enter a num: '))
# r = 0
# for i in range(n+1):
#     r += i
# print(r)

# L7 (multiplication table of n)

# n = int(input('Enter a  num : '))
# r = 1 
# for i in range(1, 11):
#     print(n * i)

# L8 (more on range() and for loop without range())
# L9 (formtted Printing)

# for x in range(10):
    # print(x, end = " ")

# n = int(input('Enter a num'))
# for i in range (1,11):
#     # print(n, 'X', i, '=', n * i)
#     # print(f'{n} X = {n * i}')
#     # print('{0} X {1} = {2}'.format(n, i, n*i))

# pi = 22/7
# print(f'value of pi = {pi:.3f}')
# print('value of pi = {0:.4f}'.format(pi))
# print('value of pi = %f:.5f' % (pi))

# L10 (do all the problem mentioned in l4 using for loop)
# L11 (nested for loop)
# L12 (Tutorial on nested loops)
# L13 (break, continue and pass)
# L14 (Conclusion)