"""
Task

You're given a substring s of some cyclic string. What's the length of the smallest possible string that can be concatenated to itself many times to obtain this cyclic string?
Example

For s = "cabca", the output should be 3

"cabca" is a substring of a cycle string "abcabcabcabc..." that can be obtained by concatenating "abc" to itself. Thus, the answer is 3.
Input/Output

    [input] string s

Constraints: 3 ≤ s.length ≤ 15.

    [output] an integer


"""


def cyclic_string(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if s in sub * 15:
                return len(sub)