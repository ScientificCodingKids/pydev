def say_hello(name):
    None # your code here

def say_hello_2(from_name, to_name):
    None # your code here

def triple(c): #compute the 3x of the input value c
    None # your code here

def do_calc(a, b, op): # add a and b if op is "ADD"; sub a and b if op is "SUB"; mult a and b if op is "MULT"; print "ERR" otherwise
    None # your code here


# sample code
def len_of_list(li): # compute the length of the list
    d = 0
    for elem in li:
        d = d + 1

    return d

def sum_of_list(li): # compute the sum of all items in a list of numbers
    None # your code here (use above len_of_list for hint on ideas)


if __name__ == "__main__":
    joe = "joe"
    moe = "moe"

    say_hello(joe) # it should print "hello, joe"
    say_hello_2(joe, moe) # it should print "joe says hi to moe"

    a = 100
    print(triple(a)) # it should print 300

    a = 6
    b = 4

    print(do_calc(a, b, "ADD")) # it should print 10
    print(do_calc(a, b, "SUB")) # it should print 2
    print(do_calc(a, b, "MULT")) # it should print 24
    print(do_calc(a, b, "DIV")) # it should print "ERR"

    sample_list = [900, 80, 7]

    print(len_of_list(sample_list)) # it should print 3
    print(sum_of_list(sample_list)) # it should print 987