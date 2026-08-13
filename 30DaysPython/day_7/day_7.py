# Day 7 - 30 Days of Python Challenge

# Exercise Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Stark Ind', 'Orion'])
it_companies.pop()
print(it_companies)
# Discard method doesn't raise errors if item is not found in the set

# Exercise Level 2
C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B
del C

# Exercise Level 3
st_age = set(age)
print(f'List Length: {len(age)}')
print(f'Set Length: {len(st_age)}') # removes duplicates

sent = 'I am a teacher and I love to inspire and teach people'
split_sent = sent.split()
print(split_sent)
st_sent = set(split_sent)
print(st_sent)
print(len(st_sent))