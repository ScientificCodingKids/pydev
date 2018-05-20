# cards: 1, 2, 3, 4
# goal: to reach 24 by doing math on the four cards given

def addz(a, b):
    print("{0} + {1} => {2}".format(a, b, a+b))
    return a+b

def subz(a, b):
    print("{0} - {1} => {2}".format(a, b, a-b))
    return a-b

def multz(a, b):
    print("{0} * {1} => {2}" .format(a, b, a*b))
    return a * b

def divz(a, b):
    print("{0} / {1} => {2}" .format(a, b, a/b))
    return a / b

if __name__ == "__main__":
    # round 1
    # 5, 2, 7, 3
    # ((5-2) + (7*3)) -- use parenthesis everywhere to mark function calls

    result = addz(subz(5, 2), multz(7, 3))
    print(result)

    #round 2
    # 3, 9, 3, 9
    # do mental math here:
    # translate to Python code
    result2 = addz( addz(3, 9), addz(3, 9))
    print(result2)

    #round 3
    # 9, 3, 6, 7
    result3 = addz( multz(7, 3), subz(9, 6))
    print(result3)


