p = float(input("Enter the Principal Amount:"))
r = float(input("Enter the Rate of Interest:"))
t = float(input("Enter the time:"))

print("\n-------------------Simple Interest------------------------------------")
si = (p*r*t)/100
amount = p + si
print("Total amount in SI = ", amount)
print("Simple Interest = ", si)

print("\n-------------------Compount Interest----------------------------------")
n = int(input("Enter the compounding periods:"))
total_amount = p * (1+r/(100*n))**(n*t)
ci = total_amount - p
print("Total amount in CI = ", total_amount)
print("Compount Interest = ", ci)