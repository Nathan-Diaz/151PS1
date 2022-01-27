#====================================================
# Filename: Prob2.py 
# 
# Your name: Nathan G. Diaz 
# Who did you work with (if anyone)?: N/A
# Estimate for time spent (in hrs)?: 1
#====================================================

# Define negate here: add "un" to the input
def negate(s):
    n = 'un'
    j = s
    return n + j

# Define intensify here: add "plus" to the input
def intensify(s):
    n = 'plus'
    j = s
    return n + j

# Define reinforce here: add "double" to the input
def reinforce(s):
    n = 'double'
    j = s
    return n + j

if __name__ == '__main__':
    # I've included the example in the description here for you to test against!
    print(negate("cold"))
    print(intensify("cold"))
    print(reinforce(intensify("cold")))
    print(reinforce(intensify(negate("good"))))
