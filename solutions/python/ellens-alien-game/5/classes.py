"""Solution to Ellen's Alien Game exercise."""


class Alien:
    x_coordinate = 0
    y_coordinate = 0
    health = 3

    total_aliens_created = 0

    string = "Hello!"

    def __init__(self, location_x, location_y):
        self.x_coordinate = location_x
        self.y_coordinate = location_y

    def hit(self):
        self.health -= 1 if self.health > 0 else 0

    def is_alive(self):
        return self.health > 0
    
    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y
    
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    #TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
    def collision_detection(self, other_object):
        pass

    def total_aliens_created(self):
        Alien.total_aliens_created += 1

def new_aliens_collection(list_of_coordinates):
    return {Alien(coordinate_x, coordinate_y) for coordinate_x, coordinate_y in list_of_coordinates}



