# Addition function
def add_numbers(a, b):
    return a + b

# Average function
def calculate_average(a, b):
    return (a + b) / 2

# Triangle area function
def triangle_area(base, height):
    return 0.5 * base * height

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

finalAddition =  add_numbers(num1, num2)
finalAverage = calculate_average(num1, num2)
finalArea = triangle_area(num1, num2)

# Calculate and print results
print("Addition: ", finalAddition)
print("Average: ", finalAverage)
print("Area of triangle: " , finalArea)