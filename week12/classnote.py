# Feng's remark
# In past two weeks, we learned how to create single functions and how to use them indivisually
# today, we show
# 1) use function written by somebody else -- e.g. math.factorize()
# 2) call same function twice with different arguments -- e.g. in perm2(), math.factorize() called with n, n-m
# 3) nested function calls with any structure -- e.g. calc24

import math

def sum(n):
    # 1 + 2 + 3 + ... + n
    z = 0
    for c in range(1, n+1):
        z = z + c
    return z

def perm1(n, m):
    # permutation(n, m) := n * (n-1) * .. * (n-m+1) (m numbers)
    # code it up using for loop
    z = 1
    for c in range(n, n-m, -1):
        z = z * c
    return z


def perm2(n, m):
    # use math.factorial() to help you
    # you are not allowed to use a loop
    # p(n, m) = n * (n-1) * .. * (n-m+1)
    # c1 = fac(n) = n * (n-1) * (n-2) * .. * (n-m) * (n-m-1) * .. * 2 * 1
    # c2 = fac(m) =                          (n-m) * (n-m-1) * .. * 2 * 1
    #
    c1 = math.factorial(n)
    c2 = math.factorial(n- m)
    return c1 / c2


if __name__ == "__main__":
    # factorial(n) := n * (n-1) * (n-2) * .. * 2 * 1

    print(math.factorial(3)) # how to call other's function

    print(perm1(5, 3), perm2(5, 3)) # they are equal

