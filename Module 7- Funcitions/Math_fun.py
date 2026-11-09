import random
#function to display a welcome message
def display_message():
    print("Welcome to the games!")

#funcition to ask the user if they would like to add or subtract 
def add_or_subtract():
    response = input=("Would you like to add or subtract or Multiply or Divide? ")
    if response == "add":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Add together {num1} and {num2}: ")
        response_add = int(input("Type your anwser here: "))
        if response_add == add(num1, num2):
            print("Yay you got it!")
        else:
            print("Sorry thats not it")
            #Subtraction 

    if response == "subtract":
        num3 = random.randint(1, 100)
        num4 = random.randint(1, 100)
        print(f"subtract {num3} and {num4}: ")
        response_sub = int(input("Type your anwser here: "))
        if response_sub == sub(num3, num4):
            print("Yay you got it!")
        else:
            print("Sorry thats not it")
#Multiply
    if response == "Multiply":
        num5 = random.randint(1, 10)
        num6 = random.randint(1, 10)
        print(f"Multiply {num5} and {num6} together")
        response_multi = int(input("Type the anwser here: "))
        if response_multi == multiply(num5, num6):
            print("Yay you got it!")
    else:
        print("Sorry thats not it.")
#Divide
        if response == "Divide":
         num7 = random.randint(1, 10)
        num8 = random.randint(1, 10)
        print(f"Divide {num7} and {num8} together")
        response_Divide = int(input("Type the anwser here: "))
        if response_Divide == divide(num7, num8):
            print("Yay you got it!")
        else:
            print("Sorry thats not it.")



#add funcition
def add(a, b):
    return a + b
#Subtract funcition
def sub(a, b):
    return a - b 
#Multiply 
def multiply(a, b): 
    return a * b
#Divide
def divide(a, b):
    return a / b 
display_message()
add_or_subtract()

game_over = "not yet"
while game_over != "STOP":
    add_or_subtract
    game_over = input("Another question? (STOP if done)")