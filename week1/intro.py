# Python code is very easy to read -- close to plain English

# guess what the code below does

# "def" keyword means a new function is defined here
def calc_1(a, b):
    return a + b  # tabbing is for indentation (not whitespaces)


def calc_2(a, b):
    if a > b:
        return "bigger"
    else:
        return "smaller"

def calc_3(n):
    sum = 0
    for i in range(1, n+1): # range(a, b) means a list of numbers starting with a (included), ending with b (excluded)
        # e.g. range(1, 4) = [1, 2, 3]
        sum = sum + i

    return sum


def demo_4(name):
    print("hello, my name is " + name)


def demo_5():
    # list
    a = ["Alice", "Bo", "Celine", "David"]

    for name in a:
        print("hi, I am " + name)

    print("Now, again ...")

    for name in a.reverse():
        print("hi, my name is " + name)

    print("Is that easy!?")


# now practice on your own
def ex_0(a, b):
    c = a
    a = b
    b = c

    print("a=", a, "b=", b)

#what is above doing? why? try:

ex_0(1, 2)

ex_0(11, 22)

ex_0(22, 11)


def ex_1(name):
    if name == "Ellen":
        return "yes!"
    else:
        return "no"

name = "" # put your name in double quote
print(ex_1(name))


def ex_2(name):
    if name in ["Brayden", "Collin", "Thomas", "Daniel", "Chloe", ]:
        return "woohoo!"
    else:
        return "ouch"

print(ex_2(name))


def ex_3(n):
    z = 0
    for i in range(1, n):
        z = z * i
    return z

print(ex_3(5))


def ex_4(n):
    z = 2
    for i in range(1, n):
        z = z * i

    return z

print(ex_4(5))

def ex_5(n):
    z = 1
    for i in range(1, n):
        z = z * i + 1

    return z

print(ex_5(5))

print(ex_5(ex_4(3)))

print(ex_4(ex_5(3)))


def ex_6(n):
    a = ["foo", "bar", "boo"]
    for i in range(1, n):
        a.reverse() # reverse itself

    return a

print(ex_6(100))

print(ex_6(1001))


def ex_7(n):
    # calculate 1*1 + 2*2 + 3*3 + ... + n*n
    s = 0
    for i in range(1, None): #replace all None with your code!
        s = s + None

    return s


def ex_8(n):
    # calculate 1*1 + 3*3 + 5*5 + ... + (2*n-1) * (2*n-1)
    s = 0
    for i in range(1, n):
        s = s + None

    return s


def ex_9(n):
    #what does this function compute?
    if n == 1 or n==0:
        return 1
    else:
        return ex_9(n-1) * ex_9(n-2)