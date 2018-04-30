def hello():
    print("say hello!")

def hello_with_name(name):
    print("hello {0}".format(name))

def addz(a, b):
    return a + b


# puzzles
def mult(a, b):
    # compute a times b

def full_name(first, last):
    #print the full name

def sum_over_list(a):
    # a is a list of numbers, compute the sum of all items

def mult_over_list(a):
    pass

def morse_code(input):
    pass

if __name__ == "__main__":
    hello()
    hello_with_name("Feng")

    c = addz(1, 2)

    c2 = addz(1, addz(3, 4))

    print(c, c2)

