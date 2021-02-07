import time

while(True):

    print("Type '1' to add.")
    print("Type '2' to subtract.")
    print("Type '3' to multiply.")
    print("Type '4' to divide.")

    operation = int(input("Which operation do you choose? "))

    num1 = int(input("Please enter your first number. "))
    num2 = int(input("Please enter your second number. "))

    if(operation == 1):
        print(num1+num2)
    elif(operation == 2):
        print(num1-num2)
    elif(operation == 3):
        print(num1*num2)
    elif(operation == 4):
        print(num1/num2)
    else:
        print("Error: Unknown operation.")

    time.sleep(1)
