print("~~~~~~~~~~~~~~~~~~Mini Calculator~~~~~~~~~~~~~~~~~~~~")

num1 = float(input("Enter First number here:   "))
num2 = float(input("Enter Second number here:  "))
print("Press 1 for Addition: ")
print("Press 2 for Subtraction: ")
print("Press 3 for Multiplication: ")
print("Press 4 for Division: ")
choice = int(input("Enter your Choice number from above: "))
if choice == 1:
    print( "The Addition of give two numbers  is: ", num1+num2)
elif choice == 2:
    print("The Subtraction of given two numbers: " ,num1-num2)
elif choice == 3:
    print("The Multiplication  of given tow numbers: " ,num1*num2)
elif choice == 4:
    print("The Division of given two numbers: ",num1/num2)
else:
    print("Invalid Input")
