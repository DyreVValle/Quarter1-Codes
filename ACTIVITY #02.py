x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
roundeddistance = round(distance, 2)
print("The distance between the two points is:", roundeddistance)