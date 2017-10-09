from random import randint
from datetime import datetime

firstNames = ['Susan', 'Dawn', 'Ottie', 'Maria', 'Bill', 'John']
lastNames = ['Smith', 'Doe', 'Brown', 'Black', 'Red', 'White', 'Messi']

def get_random_person():
    fname = firstNames[randint(0, len(firstNames) - 1)]
    lname = lastNames[randint(0, len(lastNames) - 1)]
    birthdate = datetime(randint(1900, 2017), randint(1, 12), randint(1, 28), 0, 0, 0)
    
    return {'fname': fname,
            'lname': lname,
            'birthdate': birthdate
            }