"""Task.

Calculate area of given triangle. Create a function t_area that will take a string which will represent triangle, find area of the triangle, one space will be equal to one length unit. The smallest triangle will have one length unit.

Hints

Ignore dots.

All triangles will be right isoceles.

Example:

.
.      .
.      .       .      ---> should return 2.0

.
.      .
.      .       .
.      .       .      .      ---> should return 4.5
"""


def t_area(t_str):
    a = -2
    for i in t_str:
        if i == "\n":
            a += 1
    return (a ** 2) / 2
