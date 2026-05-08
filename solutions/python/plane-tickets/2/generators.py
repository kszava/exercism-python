"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    seat_characters = ['A','B','C','D']

    for next_number in range(number):
        yield seat_characters[next_number % 4]



def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    seat_characters = ['A','B','C','D']

    if number >= 13:
        number += 4 #we are pushing forward 4 seats for row 13

    for next_number in range(number):
        row = next_number // 4 + 1 # quotient
        if row == 13: 
            continue
        yield str(row) + seat_characters[next_number % 4]


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    result = {}
    
    for next_passengers in passengers:
        seat_allocator = generate_seats(len(next_passengers))
        result.update(dict(zip(passengers, [*seat_allocator])))

    return result

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for next_seat in seat_numbers:
        remainder_zero_str = '0' * (12 - len(next_seat) - len(flight_id))
        yield next_seat + flight_id + remainder_zero_str
