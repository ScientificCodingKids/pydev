def compute_total_area(a_bot_left, a_top_right, b_bot_left, b_top_right):
    # compute the total area of the two rectangles and return it
    return None

def detect_overlap(a_bot_left, a_top_right, b_bot_left, b_top_right):
    # return True if the two rectangles overlap; return False if not
    return None


if __name__ == "__main__":
    total_area = compute_total_area((1, 0), (2, 1), (3, 0), (4, 1))
    if total_area == 2:
        print("congrats, the total area is correct")
    else:
        print("oops! please compute again!")

    is_overlapped = detect_overlap((1, 0), (2, 1), (3, 0), (4, 1))
    if is_overlapped:
        print("sorry, these two are not overlapped. check your code!")
    else:
        print("you got it right!")

    s_overlapped = detect_overlap((1, 0), (4, 2), (3,1), (5, 3))
    if not(is_overlapped):
        print("sorry, these two are overlapped. check your code!")
    else:
        print("you got it right!")