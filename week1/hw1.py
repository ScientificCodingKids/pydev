# instructions:
# step 1. Before you run the program in PyCharm, write down what you think the program will print (from ex1() )
# step 2. Run the program in PyCharm (be sure you run hw1, not some other), compare what you just wrote down
# step 3. Figure out a way to run ex2(), not run ex1() when running the program.
#  hint: think why ex1() is called? See the bottom of the code.
# step 4. Uncomment (remove all leading # symbol) for all lines within ex3() method
# step 5. Figure out a way to run ex3(). Be aware, PyCharm will throw errors as the code has bugs there! Fix all of them!
# step 6. Fun time! Figure out a way to run echo(), type your name (or whatever you like) as directed by TODO there
#  run echo(), see what is printed out, try different inputs and have fun!

def ex1():
    print("ex1")
    print("I like Python")


def ex2():
    print("ex2: congrats! You successfully run ex2() method")


#def ex3():
    #print("ex3: this method has bugs, FIX ME!")
    #print("good code or not')
    #print(""I do not know nothing", the young man said")
    #print("I need print ONE double-quote symbol next line")
    #print(""")


def echo():
    name = "" # <== TODO: put your name within the double quote

    s = "my name is {0}, if you spell all the letters inversely, it is {1}".format(name, name[-1::-1])
    print(s)

# use structure below to run a method automatically when you this file
# by default, we run ex1() method
if __name__ == "__main__":
    ex1()
