"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

"""
import re


def to_camel_case(text):
    new = [i.capitalize() for i in re.split(r'[-_]', text)]
    if text and text[0].islower(): new[0] = new[0].lower()
    return ''.join(new)