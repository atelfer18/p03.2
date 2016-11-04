"""
Problem:

    In another popular word game, players are tasked with making the longest
    words possible using a set of letters.  The score for each word is given
    calculated on the following basis:

    * Each use of q, x, y or z is awarded 2 points.
    * No points are awarded for the use of vowels.
    * All other letters score 1 point.

    For example, "question" would score 5 points: 2 for q, 1 each for s, t and n.

    The function 'scorer' takes a word as input, and should print the score
    for that word.

Tests:

    >>> scorer("question")
    5
    >>> scorer("examples")
    6
    >>> scorer("xylophone")
    8
    >>> scorer("tesselate")
    5

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)
## if using char remember to put in not == so it will check against each letter
    ##otherwise it tries to find a match in all the words

    ## when practising we put char instead of the 0 , 1, or 2 this meant it over
    ## rode the answer each time so use the number instead

# Edit this code
def scorer(word):

    count = 0

    for char in word:
        
        if char in "aeiou":
            count = count + 0

        elif char in "qxyz":
           count = count + 2

        else:
           count = count + 1



    print(count)
