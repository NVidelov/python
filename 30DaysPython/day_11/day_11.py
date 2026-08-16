# Day 11 - 30 Days of Python Challenge

# Exercise Level 1

def add_two_numbers(num1, num2):
    return num1 + num2

def area_of_circle(r):
    return 3.14 * r**2

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            print(f'{num} is not a number.')
            continue
        sum += num
    return sum

def convert_celsius_to_fahrenheit(temp_C):
    return (temp_C * 9/5) + 32

def print_list(lst1):
    for item in lst1:
        print(item)

def reverse_list(lst1):
    rev_list = []
    for i in range(len(lst1)-1,-1,-1):
        rev_list.append(lst1[i])
    return rev_list

def capitalize_list_items(lst1):
    cap_list = []
    for item in lst1:
        cap_list.append(item.capitalize())
    return cap_list

def add_items(lst1, add_item):
    lst1.append(add_item)
    return lst1

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']

def remove_item(lst1, r_item):
    lst1.remove(r_item)
    return lst1

def sum_of_numbers(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
