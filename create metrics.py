def list_creator(n, m):
    metrix = []
    for num in range(m):
        metrix.append([])
    for j in range(m):
        for i in range(n):
            metrix[j].append(i * j)
    return metrix


n = int(input('number of columns: '))
m = int(input('number of rows: '))
print(list_creator(n, m))
