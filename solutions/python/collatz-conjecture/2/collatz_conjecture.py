
def steps(number):
    if number > 0:
        return loop_steps(number, 0)
    else:
        raise ValueError("Only positive integers are allowed")


def loop_steps(number, count):
    if number % 2 == 0:
        return loop_steps(number / 2, count+1)
    elif number == 1:
        return count
    else:
        return loop_steps(number*3+1, count+1)