import random

def create_ten_random_exercises():
    ten = ''
    for i in range(10):
        ten += create_random_exercise() + '\n'
    return ten

def create_random_exercise():
    while True:
        exercise = ''
        for i in range(3):
            digit = str(random.randint(1, 100))
            operation = random.choice([' + ', ' - '])
            exercise += digit + operation
        digit = str(random.randint(1, 100))
        exercise += digit
        if eval(exercise) < 100:
            return exercise + ' = ?'
