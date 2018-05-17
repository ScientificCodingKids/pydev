def find_min(x):
    # x is a list of numbers, return the smallest number from the list
    # e.g. x = [59, 60, 63, 99, 62]
    # e.g. x = [63, 99, 60, 59, 62]
    m = x[0] # store the minimum in this variable
    for a in x:
        if a < m:
            m = a
    return m

def find_max(x):
    # x is a list of numbers, return the smallest number from the list
    # e.g. x = [59, 60, 63, 99, 62]
    # e.g. x = [63, 99, 60, 59, 62]
    m = x[0] # store the max in this variable
    for a in x:
        if a > m:
            m = a
    return m

if __name__ == "__main__":
    one = [1]
    print(find_min(one))

    y1 = [1, 2]
    y2 = [2, 1]
    z1 = [2, 1, 3]
    print(y1, "the smallest number in the list is: ", find_min(y1))
    print(y2, "the smallest number in the list is: ", find_min(y2))
    print(z1, "the smallest number in the list is: ", find_min(z1))


    x1 = [59, 60, 63, 99, 62]
    print(x1, "the smallest number in the list is: ", find_min(x1))

    x2 = [63, 99, 60, 59, 62]
    print(x2, "the smallest number in the list is: ", find_min(x2))

    # bonus question: above in "main", there are a lot of duplication
    # as we repeatedly create a list and check some calculation on this list
    # how to make the code shorter?
    # hint: use list!


