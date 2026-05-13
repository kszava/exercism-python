def get_no_unique_sides(sides, limit):
    set_side = set(sides)
    return len(set_side) == limit and 0 not in set_side

def is_triangle(sides):
   [a, b, c] = sides
   return a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    return get_no_unique_sides(sides, 1)


def isosceles(sides):
    return (get_no_unique_sides(sides, 1) or get_no_unique_sides(sides, 2)) and is_triangle(sides)


def scalene(sides):
    return get_no_unique_sides(sides, 3) and is_triangle(sides)

