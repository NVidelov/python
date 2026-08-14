# Day 10 - 30 Days of Python Challenge

'''# Exerise Level 1
for num in range(11):
    print(num)

n = 0
while n <= 10:
    print(n)
    n += 1'''

'''for num in range(1,8):
    if num == 1:
        print('#')
    elif num == 2:
        print('##')
    elif num == 3:
        print('###')
    elif num == 4:
        print('####')
    elif num == 5:
        print('#####')
    elif num == 6:
        print('######')
    else:
        print('#######')'''

'''for num in range(1,9):
    print('# # # # # # # #')'''

'''for num in range(11):
    print(f"{num} x {num} = {num**2}")'''

'''lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in lst:
    print(skill)'''

# Exercise Level 2
sum = 0
for n in range(101):
    sum += n
else:
    print(f'The sum of all numbers is {sum}.')

even_sum = 0
odd_sum = 0
for n in range(101):
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n
else:
    print(f'The sum of all even numbers is {even_sum}. The sum of all odd numbers is {odd_sum}')

# Exercise Level 3
