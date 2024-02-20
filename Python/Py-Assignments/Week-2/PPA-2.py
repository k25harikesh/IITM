# x = float(input())

# if x > 0 and x < 10:
#     print(x + 2)
# elif x >= 10:
#     print(x * x + 2)
# else:
#     print(0.0)

x = float(input())

if x <= 0:
    print(0.0)
else:
    print(x+2 if 0 < x < 10 else (x*x+2))
