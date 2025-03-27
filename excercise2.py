def areaOfCircle(r):
    PI= 3.1416
    
    # Calculate area using formula: π * r²
    area = PI * r * r

    return area

radius = float(input("Enter the radius of the circle: "))
area = areaOfCircle(radius)

print("The area of the circle: " , area)