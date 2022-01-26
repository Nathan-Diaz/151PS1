#====================================================
# Filename: Prob2.py 
# 
# Your name: Nathan G. Diaz 
# Who did you work with (if anyone)?: N/A
# Estimate for time spent (in hrs)?: 1
#====================================================

# Define negate here
# add "un" to string
def negate(s):
    n1 = 'un'
    n2 = s
    return n1 + n2

# Define intensify here
# add "plus" to string
def intensify(s):
    n1 = 'plus'
    n2 = s
    return n1 + n2

# Define reinforce here
# add "double" to string
def reinforce(s):
    n1 = 'double'
    n2 = s
    return n1 + n2

if __name__ == '__main__':
    # I've included the example in the description here for you to test against!
    print(negate("cold"))
    print(intensify("cold"))
    print(reinforce(intensify("cold")))
    print(reinforce(intensify(negate("good"))))
