def linearsearch(a, el):
    ar = []
    for i in range(len(a)):
        if a[i] == el:
            ar.append(i)
    return ar

a = [12, 11, 44, 32, 23, 1, 8, 5]
res = linearsearch(a, 23)

for i in res:
    print(i, end="")
