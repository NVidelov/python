# Day 5 - 30 Days of Python Challenge

empty_list = list()
list1 = ['item1', 'item2', 'item3', 'item4', 'item5']
print(len(list1))
print(f'First item {list1[0]}, middle item {list1[2]}, last item {list1[-1]}.')

mixed_data_types = ['Niko', 37, 'Madrid']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(f'First {it_companies[0]}, middle {it_companies[3]}, last {it_companies[-1]}')
it_companies[5] = 'Relativity'
print(it_companies)
it_companies.append('LinkedIn')
it_companies.insert(4, 'Proton')
it_companies[0] = it_companies[0].upper()
print("#; ".join(it_companies))

print('Proton' in it_companies)

it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

del it_companies[0:3]
print(it_companies)
del it_companies[3:6]
print(it_companies)
del it_companies[1]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

full_stack = joined_list.copy()
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

# Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(min(ages))
print(max(ages))
print(f'Median Age is {ages[5]}')

sum_ages = sum(ages)
len_ages = len(ages)
avg_ages = sum_ages/len_ages
print(f'Average age is {sum_ages/len_ages}.')
print(f'Range of ages is {max(ages) - min(ages)}')

print(f'Min-Avg {abs(min(ages)-avg_ages)}, Max-Avg {abs(max(ages)-avg_ages)}')