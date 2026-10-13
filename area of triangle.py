triangle = input("Enter the Type of triangle:")

if triangle == "Equilateral":
    side = float(input("Enter the side of equilateral traingle:"))
    area = (3**0.5)*side/4

elif triangle == "Right-Angled":
    base = float(input("Enter the base of right angled triangle:"))
    height = float(input("Enter the hright of right angled triangle:"))
    area = 0.5*base*height

elif triangle == "Isosceles":
    a = b = float(input("Enter the equal side:"))
    c = float(input("Enter the non-equal side:"))
    s = (a+b+c)/3
    area = (s*(s-a)*(s-b)*(s-c))**0.5

elif triangle == "Scalen":
    x = float(input("Enter the first side:"))
    y = float(input("Enter the second side:"))
    z = float(input("Enter the third side:"))
    sp = (x+y+z)/3
    area = (sp*(sp-x)*(sp-y)*(sp-z))**0.5

else:
    print("Invalid input")

print("Area of triangle:",area)