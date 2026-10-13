triangle = input("Enter the Type of triangle:")

if triangle == "Equilateral" or triangle == "equilateral" :
    side = float(input("Enter the side of equilateral traingle:"))
    area = (3**0.5)*(side**2)/4
    print("Area of triangle:",area)

elif triangle == "Right-Angled" or triangle == "right angled" :
    base = float(input("Enter the base of right angled triangle:"))
    height = float(input("Enter the hright of right angled triangle:"))
    area = 0.5*base*height
    print("Area of triangle:",area)

elif triangle == "Isosceles" or triangle == "isosceles":
    a = b = float(input("Enter the equal side:"))
    c = float(input("Enter the non-equal side:"))
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of triangle:",area)

elif triangle == "Scalen" or triangle == "scalen":
    x = float(input("Enter the first side:"))
    y = float(input("Enter the second side:"))
    z = float(input("Enter the third side:"))
    sp = (x+y+z)/2
    area = (sp*(sp-x)*(sp-y)*(sp-z))**0.5
    print("Area of triangle:",area)

else:
    print("Invalid input")
#this way there is no error left from my side but i am trying to learn more so if possible i make it more accurate.
