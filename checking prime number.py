num = int(input("Enter a number to check if it is prime or not:"))
if num<2:
    print("Not prime number neither a compostie number")
else:
    prime = True
    for i in range(2,num):
        if num%i == 0:
            prime = False
            break
    if prime:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")