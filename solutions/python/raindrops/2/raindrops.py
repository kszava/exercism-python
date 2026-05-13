def convert(number):
    divisors = [3,5,7]
    result = [return_string(divisor) if is_divisible(number, divisor) else "" for divisor in divisors]
    cleared_result = "".join(result)
    if cleared_result == "":
        return str(number)
    return cleared_result

def is_divisible(number, divisor):
    return number % divisor == 0

def return_string(divisor_number):

    divisor = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }

    return divisor.get(divisor_number, "")
    