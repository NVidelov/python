# Day 8 - 30 Days of Python Challenge

dog = {}
dog['name'] = 'Fluffy'
dog['breed'] = 'Corgi'
dog['legs'] = 'short'
dog['age'] = 3
print(dog)

student = {
    'first_name': 'Niko',
    'last_name': 'Vee',
    'gender': 'Male',
    'age': 37,
    'marital_status': 'In a relationship',
    'skills': ['Python', 'PowerShell'],
    'country': 'Spain',
    'city': 'Madrid'
}

print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('SQL')
print(student['skills'])

print(student.keys())
print(student.values())

print(student.items())

student.pop('marital_status')
del dog