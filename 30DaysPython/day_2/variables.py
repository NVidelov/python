# Day 2 - 30 Days Of Python Challenge

first_name = "Niko"
last_name = "Vee"
full_name = "Niko Vee"
country = "Spain"
city = "Madrid"
age = 37
year = 2026
is_married = False
is_true = True
is_light_on = False
var1, var2, var3 = "Kitchen", "Bedroom", "Living Room"

# Level 2
print(type(country))
print(type(age))
print(type(is_married))

print(len(first_name))
print(len(first_name), len(last_name))

num_one, num_two = 5, 4
total = num_one+num_two
print(total)

diff = num_one-num_two
print(diff)

product = num_two*num_one
print(product)

division = num_one/num_two
print(division)

remainder = num_two%num_one
print(remainder)

exp = num_one**num_two
print(exp)

floor_division = num_one//num_two
print(floor_division)

area_of_circle = 3.14*(30**2)
circum_of_circle = 2*3.14*30
print("Area", area_of_circle)
print("Circumference", circum_of_circle)

input_radius = int(input("Enter radius: "))
input_area = 3.14*(input_radius**2)
print("Area", input_area)