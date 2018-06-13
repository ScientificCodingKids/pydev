# review selected HWs

def swap_values(): #week 3.1
    a = 'tape'
    b = 'poker'

    tmp = a
    a = b
    b = tmp

    # now a= 'poker', b = 'tape'
    print(a, b)

if __name__ == "__main__":
    swap_values()

# 1 * 2 * 3 * .. * 10

# 0*0 + 1*1 + 2*2 + ... + 10*10
def sum_of_squares(): #week 3.4
    sum = 0
    for i in range(0, 11):
        sum = sum + i * i

    print(sum)

# string: "abc"
def draw_triangle(): # week 4.2
    # w
    # ww
    # www
    # wwww
    # wwwww
    s = "w"
    for i in range(1, 6):
       print(s)
       s = s + "w"

# X
# XX
# XXX


def sum_5x(): #week 4.3
    # sum of all 5's multipliers within 1 to 100
    # 5 + 10 + 20 + .. + 100
    sum = 0
    for i in range(1, 21):
        sum = sum + 5 * i

    print(sum)


def printed_selected_items_from_dict(): # week 6.2
    all_chess_student_with_old_score = {"Xavier": 288, "Victor": 999, "Zoe": 1050}
    for name, score in all_chess_student_with_old_score.items():
        if score > 850:
            print(name)


# {"AZ": "AZ", "CA": "CA", "NJ": "NJ", "NY": "NY"}
def create_dict_from_list(): # week 6.4 #Hello I am Isabella I hax
    names_list = ["AZ", "CA", "NJ", "NY"]

    dict1 = {}
    for name in names_list:
        dict1[name] = name

    dict2 = {}
    for name in names_list:
        dict2[name] = {"state": name}

def create_list_from_dict(): # week 8.1
    d = {"a": "A", "b": "B", "c": "C"}
    li = []
    for k, v in d.items():
        li.append(k)

def len_without_len(): # week 8.2
    li = ["one", "two", "three"]
    c = 0 # count the length from 0
    for el in li:
        c = c+ 1

# week 10

def compute_the_union_line_segment(lseg1, lseg2):
    # HW
    # given two line segments
    # compute the smallest new line segment that contains both input line segments
    # e.g. for [0, 10] and [5, 15], the output should be [0, 15]
    # e.g. for [0, 15] and [5, 10], the output should be [0, 15]
    l = min(lseg1[0], lseg2[0])
    r = max(lseg1[1], lseg2[1])
    return (l, r)


def are_line_segments_overlapping(lseg1, lseg2):
    # HW
    # lseg1 and lseg2 are both length-2 lists
    # return True if and only if the two overlap
    # hint: consider the two end points for lseg2, are they within lseg1?
    return (lseg1[1] > lseg2[0]) and (lseg2[1] > lseg1[0])