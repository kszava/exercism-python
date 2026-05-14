def is_armstrong_number(number):
    number_of_digits = len(str(number))

    return sum(int(i) ** number_of_digits for i in str(number)) == number
