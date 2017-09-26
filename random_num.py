"""
Given a function that returns a random integer number between 1 and 5, create a
function that creates a random integer between 1 and 7.

Owner- Sanjay kumar
"""

import random

def random_num(r=7):
    """Returns a random number between 1 and 7.

    Args:
    `   r: max limit; default is 8. 
    """
    return int(random.randrange(1,r+1))    

    
if __name__=='__main__':
    # Generate 10 random number between 1, 7
    r = 7    # max limit
    for i in range(10):
        random_num(r)
        