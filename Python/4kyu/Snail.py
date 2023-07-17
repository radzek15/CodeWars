"""Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]]."""

# my solution
def snail(snail):
    arr=[]
    while snail:
        arr.extend(snail.pop(0)) #1st row
        if snail:
            for i in snail:
                arr.append(i.pop()) #last col
        if snail:
            arr.extend(snail.pop(-1)[::-1]) #last row
        if snail:
            for i in snail[::-1]:
                arr.append(i.pop(0))  # 1st col
    return arr

# to remember numpy rot90