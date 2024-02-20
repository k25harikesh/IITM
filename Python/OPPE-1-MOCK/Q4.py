def exact_count(para, n):

    para = para.split(' ')
    flag = False
    for x in range(len(para)):
        if para.count(para[x]) == n:
            flag = True
    return flag


print(exact_count('good word many good works good real choice', 3))
