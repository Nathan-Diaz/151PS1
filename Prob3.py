#====================================================
# Filename: Prob3.py
# 
# Your name: Nathan G. Diaz
# Who did you work with (if anyone)?: N/A
# Estimate for time spent (in hrs)?: 0.5
#====================================================


from re import T


def print_multiples():
    """
    Prints all the numbers between 1 and 100 which are multiples
    of 6 and 7 but not both. One number printed per line.
    """
    t = [x for x in range(0,101,6)] #generates a list of numbers between 0 and 100 counting by 6
    s = [y for y in range(0,101,7)] #generates a list of numbers between 0 and 100 counting by 7

    r = set(t) - set(s) # creates a set, named as r, that are the numbers found in "t without the values of s"
    q = set(s) - set(t) # creates a set, named as q, that are the numbers found in "s without the values of t"

    k = list(r) + list(q) #creates a list, named as k, that are the numbers found in q and r
    print(k)



if __name__ == '__main__':
    print_multiples()
