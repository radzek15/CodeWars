"""
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:
case 	return
name equals owner 	'Hello boss'
otherwise 	'Hello guest'
"""


def how_much_i_love_you(nb):
    results = {0: 'not at all',1:"I love you",2:'a little',3:'a lot', 4: 'passionately', 5: 'madly'}
    return results[nb%6]
