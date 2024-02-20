# '''

# Accept two integers
# a and b as input and print the absolute difference of both the numbers. For example, if
# a=9,b=8, then the absolute difference is
# 9
# −
# 8
# =
# 1
# 9−8=1. So, your output should be
# 1
# 1. You should be able to solve this problem using the concepts covered in this week

# '''

# a = int(input())
# b = int(input())
# res = a-b
# if res >= 0:
#     print(res)
# else :
#     res = -1*res
#     print(res)

a = int(input())
b = int(input())
print(a-b if a > b else b-a)
