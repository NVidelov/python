# Day 12 - 30 Days of Python Challenge

# Exercise Level 1
import string
import random

def random_user_id():
    n_chars = int(input('Enter number of chars: '))
    n_ids = int(input('Enter number of IDs to generate: '))
    chars = string.ascii_letters + string.digits
    for _ in range(n_ids):
        user_id = ''.join(random.choices(chars, k=n_chars))
        print(user_id)

def rgb_color_gen():
    rgb1 = random.randint(0,255)
    rgb2 = random.randint(0,255)
    rgb3 = random.randint(0,255)
    return f"rgb({rgb1},{rgb2},{rgb3})"

# Exercise Level 2


# Exercise Level 3
def random_nums():
    lst1 = []
    while len(lst1) < 7:
        i_num = random.randint(0,9)
        if i_num not in lst1:
            lst1.append(i_num)
    return lst1