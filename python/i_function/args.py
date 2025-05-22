def getTotal(*args):
    total = 0
    for i in args:
        total += i
    return total


result = getTotal(1, 2, 3, 4, 5, 6, 7)
print(result)