import time #Lets you work with time

while(True): # A while loop lets you repeat the code forever. You should always put a delay on it to prevent freezing/crashing your computer.

    print("Type '1' to add.") #Shows the words inside of the quotation marks.
    print("Type '2' to subtract.")
    print("Type '3' to multiply.")
    print("Type '4' to divide.")

    operation = int(input("Which operation do you choose? ")) #Gets input from the user and converts it into an integer (number).

    num1 = int(input("Please enter your first number. "))
    num2 = int(input("Please enter your second number. "))

    if(operation == 1): #Checks if a condition is true (In this case, if operation is equal to 1)
        print(num1+num2) # Use + to add
    elif(operation == 2): #If all of the previous statements are false, checks another statement.
        print(num1-num2) #Use - to subtract
    elif(operation == 3):
        print(num1*num2) #Use * to multiply
    elif(operation == 4):
        print(num1/num2) #Use / to divide.
    else: #If all of the previous conditions are false...
        print("Error: Unknown operation.")

    time.sleep(1) #Delay for one second
