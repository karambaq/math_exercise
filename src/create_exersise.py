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
            digit = str(random.choice([x for x in range(11, 99) if x % 10 != 0]))
            operation = random.choice([' + ', ' - '])
            exercise += digit + operation
            if eval(exercise[:-2]) < 0 or eval(exercise[:-2]) > 100:
                break

        if eval(exercise[:-2]) not in range(1, 99):
            continue
        digit = str(random.choice([x for x in range(11, 99) if x % 10 != 0]))
        exercise += digit
        if eval(exercise) in range(1, 99):
            return exercise + ' = ?'
