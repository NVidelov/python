# Day 14 - 30 Days of Python Challenge

# Exercise Level 1

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Thor', 'Bruce', 'Marcus', 'Jill']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1
# Map - Applies the same function to every item
# Filter - Keeps only items for which the function returns True
# Reduce - Combines items into one result

# 2
# Higher-order function - Function that takes another function as an argument
# Closure - Function that remembers variables from its outer scope even after the scope is finished
# Decorator - Function that takes another function and adds behavior without changing its code

# 3
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)

# 4
""" for country in countries:
    print(country) """

# 5
""" for name in names:
    print(name) """

# 6 
""" for number in numbers:
    print(number) """

# Exercise Level 2

# 1
def upper_str(str):
    return str.upper()
countries_upper = map(upper_str, countries)
print(list(countries_upper))

# 2
def square_num(x):
    return x ** 2
squared_numbers = map(square_num, numbers)
print(list(squared_numbers))

# 3
names_upper = map(upper_str, names)
print(list(names_upper))

# 4
def country_land(country):
    if 'land' in country:
        return True
    return False
land_countries = filter(country_land, countries)
print(list(land_countries))

# 5
def six_letter_countries(country):
    if len(country) == 6:
        return True
    return False
equals_six = filter(six_letter_countries, countries)
print(list(equals_six))

# 6
def six_letter_countries_plus(country):
    if len(country) >= 6:
        return True
    return False
greater_than_six = filter(six_letter_countries_plus, countries)
print(list(greater_than_six))

# 7
def starts_with(country):
    if country.startswith('E'):
        return True
    return False
starts_with_e = filter(starts_with, countries)
print(list(starts_with_e))

# 9
def sum_nums(a,b):
    return a + b
summed_numbers = reduce(sum_nums, numbers)
print(summed_numbers)