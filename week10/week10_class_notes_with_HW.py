def say_hello(name):
    print("hello, ", name)

def addz(a, b):
    sum = a + b
    return sum

def sum_of_list(li):
    # answer to previous week HW
    s = 0
    for c in li:
        s = s + c
    return s


def is_point_within_line_segment(lseg, pt):
    # lseg: the line segment, represented as Python list of two numbers
    # pt: the point, represented by a single number
    if pt < lseg[0]:
        return False
    if pt > lseg[1]:
        return False
    return True


def is_point_within_line_segment_2(lseg, pt):
    # lseg: the line segment, represented as Python list of two numbers
    # pt: the point, represented by a single number
    return (pt >= lseg[0]) and (pt <= lseg[1])


def is_point_left_to_line_segment(lseg, pt):
    #your code here
    # it should return Boolean value (True or False)
    if pt < lseg[0]:
        return True
    else:
        return False

def is_point_left_to_line_segment_2(lseg, pt):
    #your code here
    # it should return Boolean value (True or False)
    if pt < lseg[0]:
        return True
    return False


def is_point_left_to_line_segment_3(lseg, pt):
    #your code here
    # it should return Boolean value (True or False)
    return pt < lseg[0]


def is_point_right_to_line_segment(lseg, pt):
    # HW
    return None


def compute_the_union_line_segment(lseg1, lseg2):
    # HW
    # given two line segments
    # compute the smallest new line segment that contains both input line segments
    # e.g. for [0, 10] and [5, 15], the output should be [0, 15]
    # e.g. for [0, 15] and [5, 10], the output should be [0, 15]
    return None


def are_line_segments_overlapping(lseg1, lseg2):
    # HW
    # lseg1 and lseg2 are both length-2 lists
    # return True if and only if the two overlap
    # hint: consider the two end points for lseg2, are they within lseg1?
    return None


def compute_length_of_line_segment(lseg):
    # HW
    # lseg: line segment as a length-2 list
    # e.g. for [0, 10], the output is 10
    # e.g. for [1, 9], the output is 8
    # bonus requirement: we require lseg[0] < lseg[1], i.e. left end pt should show up first
    # check if it is the case, if not, print "ERR" and return None
    return None


if __name__ == "__main__":
    #say_hello("Feng")
    sample_list = [1, 22, 333]
    print(len(sample_list))
    #sum = sum_of_list(sample_list)
    #print("the sum of the list is ", sum)
    line_segment = [0, 10]
    pt1 = 5
    pt2 = -2
    pt3 = 15

    print(pt1, is_point_within_line_segment(line_segment, pt1))
    print(pt2, is_point_within_line_segment(line_segment, pt2))
    print(pt3, is_point_within_line_segment(line_segment, pt3))

    print(pt1, is_point_left_to_line_segment(line_segment, pt1))
    print(pt2, is_point_left_to_line_segment(line_segment, pt2))
    print(pt3, is_point_left_to_line_segment(line_segment, pt3))

    ls_a = [0, 10]
    ls_b = [5, 6]
    ls_c = [7, 20]
    ls_d = [12, 15]

    print("Check if two line segments overlap")
    print(ls_a, ls_b, are_line_segments_overlapping(ls_a, ls_b))
    print(ls_a, ls_c, are_line_segments_overlapping(ls_a, ls_c))
    print(ls_a, ls_d, are_line_segments_overlapping(ls_a, ls_d))

