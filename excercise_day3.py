print("Day 3 Excercices")
#1. Declare your age as interger variable
my_age = 2026 - 1998
print("my age declared as an integer is: ", int(my_age), type(my_age))

#2. Declare you height as a float variable
my_height = 185
print(f"My Declared heigt is: {my_height} and as a Float Variable is: {float(my_height)}")

#3. Declare a variable that stores a complex number
complex_variable = 9.5 + 4j
print(f"variable declared as: (complex_variable) stores {complex_variable} as a complex number")

#4. Write a script that prompts the user to enter base and height/calculate the area the triangle)
base = float(input("Enter base for the triangle "))
height = float(input("Enter height for the triangle "))
print(f"User entered Base is {base} and height is {height}")

#calculate the area the triangle (area = 0.5 x b x h)
area_of_triangle = 0.5 * (base * height)
print(f"the calculated are of the triagle based on user base and height is: {int(area_of_triangle)}")

#5. Write a script that prompts the user to enter side a,b and c of a triangle./calculate the perimeter of the triangle using (perimeter = a + b + c))
side_a = float(input("Enter Side a of the triangle "))
side_b = float(input("Enter Side b of the triangle "))
side_c = float(input("Enter Side c of the triangle "))

print(f"User entered data for side a,b and c is: {side_a}, {side_b} and {side_c} respectively")
#calculate the perimeter of the triangle (perimeter = a + b + c)
perimeter_of_triangle = side_a + side_b + side_c
print(f"perimeter of the triangle based on user prompts data is = {int(perimeter_of_triangle)}")

#6. Write a script that prompts the user to enter side a,b and c of a triangle./calculate the perimeter of the triangle using (perimeter = a + b + c))
length = float(input("Enter the Lenght  of the triangle "))
width = float(input("Enter  the width of the triangle "))
print(f"length and width of the triangle based on user prompts data is: {length} and {width} respectively")
#calculate the area of the triangle (area = lenght x width) and perimeter (perimeter = 2 x (lenghth + width)
area_of_the_triangle = length * width
perimeter_of_the_triangle = 2 *  (length + width)
print(f"Based on the above data prompts; Area of the triangle is {int(area_of_the_triangle)} and perimeter for the triangle is {int(perimeter_of_the_triangle)} respectively")

#7. Get the raduis of circle using prompt
radius_of_circle = float(input("Enter The Radius for the Circle: "))
print(f"User Entered Radius for the circle is: {radius_of_circle}")
#Calculate the area (pi x r x r) and circumference (c=2 x pi x r) where pi = 3.14

#declare variable for pi
pi = 3.14
#calculate Area of the circle (area = pi x r x r)or (area = pi x r**2)
area_of_the_circle = pi * radius_of_circle ** 2
#calculate circumference of the circle (c = 2 x pi r x r)
circumference_of_the_circle = 2 * pi * radius_of_circle
print(f"based on the above data area of the circle is: {int(area_of_the_circle)} and the circumference of the circle is: {int(circumference_of_the_circle)}")

#8. Get the raduis of circle using prompt