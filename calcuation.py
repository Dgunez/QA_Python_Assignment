#Ask the user for two numbers and an operation (+, -, *, /).
#Print the result.
while True:#true is boolean value and using while loop with true keeps repeating untils we stop manually

    num1=float(input("enter first number: "))
    num2=float(input("enter second number: "))

    operation= input("enter an operation(+,-,*,/): ")

    if operation == "+":
        result= num1+num2

    elif operation =="-":
        result = num1-num2

    elif operation=="*":
        result=num1*num2

    elif operation =="/":
        if num2 !=0: #before dividing making sure the num2 is not 0
            result=num1/num2
        else:
            result= "error! cannot divide by zero."
    else:
        result="invalid operation!" #if user typed anything other than assigned operators

    print("Result: ", result)

  # Ask user if they want to continue
    choice = input("Do you want to calculate again? (yes/no): ").lower()#.lower converts whatever is types into lowercase like YES into yes
    if choice != "yes": #if entered no then prints goodbye
        print("Goodbye!")
        break  # Exit the loop
