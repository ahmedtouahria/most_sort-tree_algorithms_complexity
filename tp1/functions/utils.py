import random

def array_of_random(n):
    rand_list = []  # create empty for append array elements
    for i in range(n):
        rand_list.append(random.randint(0, 1000))
    return rand_list