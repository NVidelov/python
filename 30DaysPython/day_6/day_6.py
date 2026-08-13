# Day 6 - 30 Days of Python Challenge

# Exercise Level 1
tpl = ()    # of tuple()
bro_tpl = ('Vee', 'Thor')
sis_tpl = ('Blushweaver', 'Love')
siblings = bro_tpl + sis_tpl
print(f'Total siblings: {len(siblings)}')

lst = list(siblings)
lst.append('Gandalf')
lst.append("Athena")
fam = tuple(lst)
print(fam)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print('Iceland' in nordic_countries)