def print_my_basic_info():
    name = "Dr N"
    age = 28
    weight = 280.0
    has_voting_right = True

    print("{0} has age {1} with weight {2} pounds, he has voting right ({3})".format(name, age, weight, has_voting_right))


def run_ints():
    a = 11
    b = 22
    a, b = a * 2 + b, b - a

    print(a, b)


def run_strs():
    bro = "Lo"
    sis = "Jo"
    surname = "Ho"

    sentence = bro + " " + surname + " has a sister " + sis + " " + surname
    print(sentence)

    sentence = sis + " " + surname + " has a brother " + bro + " " + surname
    print(sentence)


if __name__ == "__main__":
    print_my_basic_info()

    run_ints()

    run_strs()
    