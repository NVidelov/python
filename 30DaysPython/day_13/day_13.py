# Day 13 - 30 Days of Python

# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
below_zero = [i for i in numbers if i <= 0]
print(below_zero)

# 2 
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for row in list_of_lists for num in row]
print(flattened_list)

# 3
result = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(result)

# 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[name.upper(), name[:3].upper(), city.upper()]
                        for row in countries
                        for name, city in row]
print(flattened_countries)

# 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [
    {'country': name.upper(), 'city': city.upper()}
    for row in countries
    for name, city in row
]
print(result)

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Barack', 'Obama')], [('Bruce', 'Wayne')]]
full_names = [f"{first} {last}" for row in names for first, last in row]
print(full_names)