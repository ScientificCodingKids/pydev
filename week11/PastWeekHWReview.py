# 2018-05-12 note:
# first we show the anawer of one HW problem of last week
# then we show a new function

def compute_length_of_line_segment(lseg):
    # HW
    # lseg: line segment as a length-2 list
    # e.g. for [0, 10], the output is 10
    # e.g. for [1, 9], the output is 8
    # bonus requirement: we require lseg[0] < lseg[1], i.e. left end pt should show up first
    # check if it is the case, if not, print "ERR" and return None

    # right - left
    right = lseg[1]
    left = lseg[0]

    if right < left:
        print("ERR")
        return None

    return right - left

def compute_length_of_line_segment_ex(a, b):
    # we only know a and b are two ends of a line segment
    # i.e. we do not know the order
    if a < b:
        return b - a
    else:
        return a - b


if __name__ == "__main__":
    #test HW answer
    print(compute_length_of_line_segment([1, 10]))
    print(compute_length_of_line_segment([10, 1]))

    # test new code on 2018-05-12
    print(compute_length_of_line_segment_ex(1, 10)) # expect 9
    print(compute_length_of_line_segment_ex(10, 1)) # expect 9