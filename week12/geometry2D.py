# tuple

# list: [1, 2, 4]

# tuple: (1, 2, 4) -- use round bracket
# we can use tuple to tell (x,y) coordinate
# origin: (0, 0)
# (3, 4) => x-coordinate is 3 and y-coordinate is 4
# syntax:

# pt : tuple
# pt[0] and pt[1] are used to get the x and y coordinate

def show_coord(pt):
    print("x-coordinate is {0} and y-coordinate is {1} ".
          format(pt[0], pt[1]))


if __name__ == "__main__":
    pt = (3, 4)
    show_coord(pt)
