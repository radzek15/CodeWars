"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false


"""


def xo(s):
    counter = 0
    for i in s.lower():
        if i == 'x':
            counter += 1
        elif i == 'o':
            counter -= 1
    return not counter
