def compute_square_len(a_bot_left, a_top_right, b_bot_left, b_top_right):
    # sample code

    # step 1. get all x-coordinates for all four nodes
    x_a_bot_left = a_bot_left[0]
    x_a_top_right = a_top_right[0]

    x_b_bot_let = b_bot_left[0]
    x_b_top_right = b_top_right[0]


    #your code

    # step 2, compute the bracket on x direction, x_l and x_r
    x_l = min(x_a_bot_left, x_a_top_right, x_b_bot_let, x_b_top_right)
    x_r = max(x_a_bot_left, x_a_top_right, x_b_bot_let, x_b_top_right)

    # step 3, do step 1 for y-coordinates

    y_a_bot_left = a_bot_left[1]
    y_a_top_right = a_top_right[1]

    y_b_bot_left = a_bot_left[1]
    y_b_top_right = a_top_right[1]

    # step 4, do step 4 for y direction

    y_l = min(y_a_bot_left, y_a_top_right, y_b_bot_left, y_b_top_right)
    y_r = max(y_a_bot_left, y_a_top_right, y_b_bot_left, y_b_top_right)

    x_len = x_r - x_l
    y_len = y_r - y_l

    square_len = max(x_len, y_len)

    return square_len


if __name__ == "__main__":
    r = compute_square_len((1,0), (2,1), (3,0), (4,1))
    print(r)