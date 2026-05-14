import math

SCORE_SYSTEM = [(10, (1,1)), (5, (5,5)), (1, (10,10))]

def score(x, y):
    # Calculate straight-line distance from center
    distance = math.sqrt(x**2 + y**2)
    return next((value for (value, next_score) in SCORE_SYSTEM if distance <= next_score[0]), 0)