"""
 No description

 Returns n-th array value to the power of itself
 """


def index(array, n):
    return array[n]**n if len(array) > n else -1
