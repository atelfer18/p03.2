"""
Problem:

    We need to count the number of vowels present in a string.
    The function `vowels` should take a string and print out
    the number of vowels it contains.

Tests:

    >>> vowels("hello")
    2
    >>> vowels("world")
    1
    >>> vowels("why")
    0
    >>> vowels("beautiful")
    5

"""


# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def vowels(word):

    count = 0

    for char in word:
        if char =="a" or char =="e" or char =="i" or char =="o" or char =="u":

            count = count + 1
    print(count)

