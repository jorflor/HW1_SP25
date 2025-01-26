# region imports
#This way of importing is saying from (the module) random, import (the function) random
#Other ways of importing might be:  import random
#             In the above case, we access the function random as random.random()
#Another way to import might be:  from random import random as rnd
#             In the above case, we use rnd() to produce a random number
from random import random
# endregion

# region functions
def rollFairDie():
    """
    This function simulates rolling a fair die such that the probability of each integer is 1/6.
    :return: an integer between 1 and 6 inclusive
    """
    x = random()  # should be a floating point number between 0.0 and 1.0
    if x <= 1.0/6.0:
        return 1
    if x <= 2.0/6.0:
        return 2
    if x<= 3.0/6.0:
        return 3
    if x <= 4.0/6.0:
        return 4
    if x <= 5.0/6.0:
        return 5
    if x <= 6.0/6.0:
        return 6

def rollUnFairDie():
    """
    This function simulates rolling an unfair die such that the probability of rolling a 1 is 0.2. with all other
    integers having equal probability.  Now, the probability of numbers 2-6 should be 0.8/5.
    :return: an integer between 1 and 6 inclusive
    """
    p=0.2
    x=random()
    if x <= p:
        return 1
    if x <= (p+(1-p)/5.0):
        return 2
    if x <= (p+2*(1-p)/5.0):
        return 3
    if x <= (p+3*(1-p)/5.0):
        return 4
    if x <= (p+4*(1-p)/5.0):
        return 5
    if x <= (p+5*(1-p)/5.0):
        return 6
# endregion

# The if statement below is known as: main guarding
if __name__ == "__main__":
    x = rollFairDie()
    print(x)