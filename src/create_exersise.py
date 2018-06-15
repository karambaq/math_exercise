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
            digit = str(random.randint(10, 99))
            operation = random.choice([' + ', ' - '])
            exercise += digit + operation
            if eval(exercise[:-2]) < 0 or eval(exercise[:-2]) > 100:
                break

        if eval(exercise[:-2]) not in range(0, 99):
            continue
        digit = str(random.randint(10, 99))
        exercise += digit
        if eval(exercise) in range(0, 99):
            return exercise + ' = ?'
