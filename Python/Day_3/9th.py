choice=int(input("Enter 1 for IN to US \nEnter 2 for celsius to fahrenheit\nEnter 3 for BMI calculation\nEnter 4 for simple Interest Calculation :"))
if choice==1:
    print("Enter the amount in INR: ")
    amount=int(input())
    usd=amount/85
    print("Amount in USD is: ",usd)
elif choice==2:
    print("Enter the temperature in celsius: ")
    celsius=int(input())
    fahrenheit=(celsius*9/5)+32
    print("Temperature in fahrenheit is: ",fahrenheit)
elif choice==3:
    print("Enter the weight in kg: ")
    weight=int(input())
    print("Enter the height in cm: ")
    height=int(input())
    heightm=height/100
    bmi=weight/(heightm*heightm)
    print("BMI is: ",bmi)
elif choice==4:
    print("Enter the principal amount: ")
    p=int(input())
    print("Enter the rate of interest: ")
    r=int(input())
    print("Enter the time in years: ")
    t=int(input())
    si=(p*r*t)/100
    print("Simple Interest is: ",si)
else:
    print("Invalid choice")

