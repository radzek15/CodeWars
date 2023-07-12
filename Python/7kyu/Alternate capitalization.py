"""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity

"""


def capitalize(s):
    new_s = ''.join([i.upper() if j%2==0 else i for j,i in enumerate(s)])
    return [new_s,new_s.swapcase()]
