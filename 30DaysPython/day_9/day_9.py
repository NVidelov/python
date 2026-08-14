# Day 9 - 30 Days of Python Challenge
'''
# Exercise Level 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You're old enough to drive.")
else:
    print(f'You need {18 - age} more years before you can drive.')

my_age = 37
your_age = int(input("Enter your age: "))
if your_age > my_age and your_age - my_age == 1:
    print(f'You are {your_age - my_age} year older than me.')
elif your_age > my_age:
    print(f'You are {your_age - my_age} years older than me.')
else:
    print("We are the same age.")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} is equal to {b}.")
'''
'''
# Exercise Level 2
score = int(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else:
    print("F")

month = input("Enter the month: ")
if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")  
else:
    print("Invalid month entered.")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input("Enter a fruit name: ")
if fruit_input in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit_input)
    print(fruits)'''

# Exercise Level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    middle_skill = len(person['skills']) // 2
    print(f"The middle skill is: {person['skills'][middle_skill]}")
    if 'Python' in person['skills']:
        print("The person has Python skill.")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")