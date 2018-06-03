#
# def compute_sum_of_even(n):
#     # compute 2 + 4 + 6 + ... + 2*n (even only)
#     z = 0
#     for c in range(1, n+1):
#         print(c*2)
#         z = z + c*2
#
#     return z
#
#
# def compute_sum_of_even_chloe(n):
#     # compute 2 + 4 + 6 + ... + 2*n (even only)
#     z = 0
#     for c in range(1, 2*n+1):
#         if c % 2 == 0:
#             print(c)
#             z = z + c
#
#     return z

def compute_sum_of_odd(n):
    # compute 1 + 3 + 5 + .. + (2*n-1) (odd only)
    z = 0
    for c in range(1, n+1):
        print(c*2-1)
        z = z + c*2-1
    return z

# ATTN: you do NOT need code in is_first_digit_4() and is_last_digit_4()
# but you will need use these two to solve problem sum_skipping_4
def is_first_digit_4(n):
    return n>39 and n<50

def is_last_digit_4(n):
    m = n - int(n/10)*10
    return m == 4


def sum_skipping_4(m):
    # sum over all numbers from 1 to m, but skipping all numbers containing 4
    # e.g. m = 5 => 1 + 2 + 3 + 5
    # e.g. m = 15 => 1 + 2 + 3 + 5 + 6 + .. + 13 + 15
    # e.g. m = 51 => 1 + 2 + 3 + 5 + 6 + .. + 13 + 15 + 16 ... + 38 + 39 + 50 + 51
    # you can assume 1 <= m <= 99
    s = 0
    for c in range(1, m+1):
        if is_first_digit_4(c) == False and is_last_digit_4(c) == False:
            s = s + c
    return s

# we do some math with 2D geometry, with focus on rectangular shape

def get_opposite(pt):
    # compute the opposite pt.
    # e.g. (3, 4) -> (-3, -4); (-2, -3) -> (2, 3)
    pt2 = (0-pt[0], 0-pt[1])
    return pt2


def calc_area(pt_bottom_left, pt_top_right):
    # a rectangular shape is determined by two points: bottom left & top right
    # now we compute its width and height, hence its area, in steps
    # fill the code (currently None)
    x_left = pt_bottom_left[0]
    y_bottom = pt_bottom_left[None]

    x_right =pt_top_right[0]
    y_top = pt_top_right[None]

    width = x_right - x_left
    height = None

    area = None * height
    return area

if __name__ == "__main__":
    print("sum of even is")
    # print(compute_sum_of_even_chloe(3))
    # print(compute_sum_of_even(3))


    #print("sum of odd is")
    #print(compute_sum_of_odd(4))

    # for m in range(1, 99):
    #     print(m, "-> ", sum_skipping_4(m))

    print("opposites")
    print(get_opposite((3, -4)))