def demo_true(b):
    if b:
        print("yes, it is True")
    else:
        print("no, it is False")

def demo_not_true_is_NOT_false(b):
    if not(b):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    print(True and True)
    print(False or False)

    print(demo_true(True))

    print(demo_not_true_is_NOT_false(None))