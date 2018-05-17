# write your code below, run the program

def f(x):
    #code your function that doubles the input number
    return None


def g(x):
    #code your function that adds 1 to the input number
    return None


def compute_the_union_line_segment(lseg1, lseg2):
    # HW
    # given two line segments
    # compute the smallest new line segment that contains both input line segments
    # e.g. for [0, 10] and [5, 15], the output should be [0, 15]
    # e.g. for [0, 15] and [5, 10], the output should be [0, 15]
    return None


def compute_the_union_all(lseg_list):
    #given a list of line segments
    #e.g. [ [0, 10], [1, 9], [7, 11] ]
    # each element in the list is a line segment
    # compute the smallest new line segment that contains ALL input line segments
    lmin = None
    rmax = None
    for lse in lseg_list:
        lmin = None
        rmax = None

    return [lmin, rmax]


def find_the_student_with_highest_score(d):
    # d is a list of student name with score
    # e.g. d = [ ["Ali", 85], ["Betty", 99], ["Zoe", 90]]
    # it should return "Betty"

    # hint: it is like find_max(), but we need track who has the highest score
    # you can use the code skeleton below
    first_record = d[0]

    highest_score = None
    highest_score_name = None

    for row in d:
        name = None
        score = None
        if highest_score < score:
            # update score AND NAME
            None
            None

    return None # what should be returned here??


if __name__ == "__main__":
    print("** call functions, order matters **")
    print(f(g(10)), g(f(10))) # are the two numbers equal? why?

    print("** compute the union for two line segments **")
    #can you figure out what is good about using a loop below?
    input_with_output_list = [ [ [1, 10], [5, 15], [1, 15]],
                   [ [1, 15], [5, 10], [1, 15]],
                   [ [1, 5] , [6, 10], [1, 10]]]

    for one_input_with_output in input_with_output_list:
        input_a = one_input_with_output[0]
        input_b = one_input_with_output[1]
        correct_output = one_input_with_output[2]

        your_output = compute_the_union_line_segment(input_a, input_b)

        if your_output == correct_output:
            print("Congrats! For {0} and {1}, your answer for the union is {2}. Correct!".format(input_a, input_b, your_output))
        else:
            print("Oops! For {0} and {1}, your answer is {2}, but correct answer is {3}. Keep working!".format(input_a, input_b, your_output, correct_output))

    print("** compute the union for all **")
    all_input_with_output_list = [  [[ [1, 10] ], [1, 10]], # single element
                                    [[ [1, 10], [5, 15]], [1, 15]], # 2 elements
                                    [[ [1, 15], [5, 10]], [1, 15]], # 2 elements
                                    [[ [1, 5], [2, 10], [3, 9]], [1, 10]] # 3 elements
                                    ]

    for one_input_with_output in all_input_with_output_list:
        input_list = one_input_with_output[0]
        correct_output = one_input_with_output[1]
        your_output = compute_the_union_all(input_list)

        if your_output == correct_output:
            print("Congrats! For {0}, your get it correct, the answer is {1}.".format(input_list, your_output))
        else:
            print("Oops! For {0}, your answer is {1}, but the correct answer is {2}. Keep working!".format(input_list, your_output, correct_output))

    records = [ ["Ali", 85], ["Betty", 99], ["Zoe", 90]]
    the_name = find_the_student_with_highest_score(records)

    if the_name == "Betty":
        print("Yes, it is Betty who has highest score!")
    else:
        print("Hmm... Please try again.")
