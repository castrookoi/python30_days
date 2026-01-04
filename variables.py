#Day 2: 30 days of programming
#Exercise Level 1
print("Excercise Level 1")
first_name = "Prince"
print(first_name)
last_name = "Okoi"
print(last_name)
full_name = "Okoi Prince Eteng"
print(full_name)
country = "Nigeria"
print(country)
city = "Port harcourt"
print(city)
age = 45
print(age)
year = 2026
print(year)
is_married = True
print(is_married)
is_true = "Yes"
print(is_true)
is_light_on = "No supply yet"
print(is_light_on)
mother_maiden_name, place_of_birth, LGA_birth, false_dob, spouse_country, is_truely_married = "vincent", "Ugep", "Yakurr", "02/02/1950", "China", False
print(mother_maiden_name, place_of_birth, LGA_birth, false_dob, spouse_country, is_truely_married)

#Excercise Level 2
print("Excercise Level 2")
#check Data Type of all your variables
print("This Data Type is: ", type(first_name))
print("This Data Type is: ", type(last_name))
print("This Data Type is: ", type(full_name))
print("This Data Type is: ", type(country))
print("This Data Type is: ", type(city))
print("This Data Type is: ", type(age))
print("This Data Type is: ", type(year))
print("This Data Type is: ", type(is_married))
print("This Data Type is: ", type(is_true))
print("This Data Type is: ", type(is_light_on))
print("the lenght of my first_name is:", len(first_name))
print("in Comparison is your first_name lenght higher than your last_name?", len(first_name) > len(last_name))

#Variable Declaratin
num_one = 5 #num_one
print("num_one is:", num_one)
num_two = 4 #num_two
print("num_two is:", num_two)

#Perform Addition
total = num_one + num_two
print("num_one + num_two =", total)

#Perform Substraction
diff = num_two - num_one
print("num_two - num_one =", diff)

#Perform Multiplication
product = num_two * num_one
print("num_two * num_one  =", product)


#Perform Division
division = num_one / num_two
print("num_one / num_two =", division)

#Perform Modulus
remainder = num_two % num_one
print("num_two % num_one =", remainder)

#Perform Exponenciation
exp  = num_one ** num_two
print("num_one ** num_two =", exp)

#Perform floor_division
floor_division = num_one // num_two
print("num_one // num_two =", floor_division)

#Perform radius of a circle
radius = 30
print("declared Radius", radius)

#Calculate the area of a circle
import math #Import in other to use math.pi
area_of_circle = math.pi * radius ** 2
print("Area of Circle with radius declared @ 30 is:", area_of_circle)

#Calculate the circumference of the circle
circum_of_circle = 2 * math.pi * radius
print("Area of circumference of the circle with radius declared @ 30 is:", circum_of_circle)

#Calculate with user input !make sure to convert to interger or float.. user inputs are considered strings
#user_input
input_radius = float(input("Enter the radius of the circle "))
print("user entered radius is:", input_radius)

area_user_input = math.pi * input_radius ** 2
print("Area of the Circle Based on user input @", input_radius,"is =", area_user_input)

