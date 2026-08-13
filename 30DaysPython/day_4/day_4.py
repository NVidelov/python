# Day 4 - 30 Days Of Python Challenge

print("Thirty Days Of Python")

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:7])
print(company.find("Coding"))
print(company.replace("Coding","Python"))
print(company.replace("All", "Everyone"))
print(company.split())

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

print(company[0])
print(len(company)-1)
print(company[10])

s = "Python For Everyone"
print(s[0], s[7], s[11])
print(company[0], company[7], company[11])

print(company.find("C"))
print(company.find("F"))
print(company.rfind("i"))

sent = "You cannot end a sentence with because because because is a conjunction"
print(sent.rindex("because"))

print(company.startswith("Coding"))
print(company.endswith("coding"))

replace_string = "   Coding For All      "
print(replace_string.replace("   ", ""))

lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(lib_list))

print("I'm enjoying this challenge.\nI wonder what's next.")

print("Name\tAge\tCountry\tCity")
print("Niko\t37\tSpain\tMadrid")

radius = 10
area = int(3.14 * radius ** 2)
print(f'The area of a circle with radius {radius} is {area} meters square.')

a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))