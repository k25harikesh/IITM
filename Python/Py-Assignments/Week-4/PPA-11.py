L = [1.1, 2.2, 3.3]


def solution(L):
    # Enter your solution below this line
    # Indent your entire code by one unit (4 spaces) to the right
    sorted_L = []
    while L:
        max = L[0]
        for x in L:
            if x > max:
                max = x
        sorted_L.append(max)
        L.remove(max)
    # Enter your solution above this line
    return sorted_L


print(
    solution(L)
)
