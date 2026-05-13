def square(number):
    if 0 < number < 65:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    return sum([square(number) for number in range(1,65)])
