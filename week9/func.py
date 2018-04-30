def addz(a, b): # the two parameters are a and b
    return a + b


def addz2(x, y): # the two parameters are x and y
    return x + y

# the above two functions are doing the same
# when we use the Python function, we "substitute" the parameters by the arguments
# -- they are matched by order, not by name
# in this sense, only the order of the paramters matter
# we can IMAGINE (not real Python code) we define a function to do above as
#def addz(_1, _2):
#   return _1 + _2


def subz(a, b):
    return a - b


if __name__ == "__main__": #this line is the Python way of defining main() function
    a = 5
    b = 4

    print(addz(a, b)) # call the function with argument a(=5) and b(=4)
    # substitution:
    # addz(a, b):
    # parameter a <- argument a = 5
    # parameter b <- argument b = 4
    # parameter a + parameter b = 5 + 4 = 9

    print(addz2(a, b)) # it prints 9
    # substitution:
    # addz(x, y):
    # parameter x <- argument a = 5
    # parameter y <- argument b = 4
    # parameter x + parameter y = 5 + 4 = 9

    #print(addz(x, y)) # ERR, as variables are not defined in main
    #print(addz2(x, y)) #ERR, as variables are not defined in main

    print(subz(a, b))
    # substitution:
    # subz(a, b):
    # parameter a <- argument a = 5
    # parameter b <- argument b = 4
    # parameter a - parameter b = 5 - 4 = 1

    print(subz(b, a))
    # substitution:
    # subz(b, a):
    # parameter b <- argument a = 5
    # parameter a <- argument b = 4
    # parameter a - parameter b = 4 - 5 = -1
    