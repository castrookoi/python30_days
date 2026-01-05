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
print(f"the calculated are of the triagle based on user base and height is: {area_of_triangle}")

#5. Write a script that prompts the user to enter side a,b and c of a triangle./calculate the perimeter of the triangle using (perimeter = a + b + c))
side_a = float(input("Enter Side a of the triangle "))
side_b = float(input("Enter Side b of the triangle "))
side_c = float(input("Enter Side c of the triangle "))

print(f"User entered data for side a,b and c is: {side_a}, {side_b} and {side_c} respectively")
#calculate the perimeter of the triangle (perimeter = a + b + c)
perimeter_of_triangle = side_a + side_b + side_c
print(f"perimeter of the triangle based on user prompts data is = {perimeter_of_triangle}")

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the Lenght  of the rectangle "))
width = float(input("Enter  the width of the rectangle "))
print(f"length and width of the rectangle based on user prompts data is: {length} and {width} respectively")

#calculate the area and perimeter
area_of_rectangle = length * width
perimeter_of_rectangle = 2 *  (length + width)
print(f"Based on the above data prompts; Area of the rectangle is {area_of_rectangle} and perimeter for the rectangle is {perimeter_of_rectangle} respectively")

#7. Get the raduis of circle using prompt
radius_of_circle = float(input("Enter The Radius for the Circle: "))
print(f"User Entered Radius for the circle is: {radius_of_circle}")

#Calculate the area (pi x r x r) and circumference (c=2 x pi x r) where pi = 3.14
pi = 3.14
area_of_the_circle = pi * radius_of_circle ** 2
circumference_of_the_circle = 2 * pi * radius_of_circle
print(f"based on the above data area of the circle is: {area_of_the_circle} and the circumference of the circle is: {circumference_of_the_circle}")

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept = 1
print("Slope is:", slope)
print("x-intercept is:", x_intercept)
print("y-intercept is:", y_intercept)

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope_points = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Slope between points:", slope_points)
print("Euclidean distance:", distance)

#10. Compare the slopes in tasks 8 and 9.
print("Are slopes the same?", slope == slope_points)

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print("When x = -3, y =", (-3)**2 + 6*(-3) + 9)
print("When x = 0, y =", 0**2 + 6*0 + 9)
print("When x = -6, y =", (-6)**2 + 6*(-6) + 9)
# y = 0 when x = -3

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("Length of python:", len('python'))
print("Length of dragon:", len('dragon'))
print("Are lengths equal?", len('python') == len('dragon'))   # False - this is falsy

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("Is 'on' in both?", 'on' in 'python' and 'on' in 'dragon')

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
print("Is jargon in sentence?", 'jargon' in sentence)

#15. There is no 'on' in both dragon and python
print("No 'on' in both?", not ('on' in 'python' and 'on' in 'dragon'))

#16. Find the length of the text python and convert the value to float and convert it to string
python_length = len('python')
print("Length as float:", float(python_length))
print("Length as string:", str(python_length))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number: "))
print("Is it even?", number % 2 == 0)

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("7 // 3 == int(2.7)?", 7 // 3 == int(2.7))

#19. Check if type of '10' is equal to type of 10
print("type('10') == type(10)?", type('10') == type(10))

#20. Check if int('9.8') is equal to 10
print("int(9.8) == 10?", int(9.8) == 10)   # Note: int('9.8') go give error, so we use 9.8

#21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print("Your weekly earning is", pay)

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

#23. Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

#8. Get the raduis of circle using prompt