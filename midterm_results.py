#Austin White
#Date: 11/2/26
#Midterm python code the "Mathanater2000"

results = []
print("Welcome to the Mathenator2000")
print()
print("Please choose from the following menu: ")
print("1. Compute area of a circle")
print(" 2. Compute area of a rectangle")
user_input = int(input("Enter Here: "))
#circle math 
if user_input == 1:
    circle_r = float(input("What is the radius of the circle? "))
    area_c = 3.14 * circle_r * circle_r
    print(area_c)
    results.append(area_c)
#Rectangle math
elif user_input == 2:
    length_r = float(input("What is the length of the rectangle? "))
    width_r = float(input("What is the width of the rectangle? "))
    area_r = length_r * width_r 
    print(f"The area of the rectangle is {area_r}")
    results.append(area_r)

#play again?
play_a = str(input("Would you like to play again (y/n)? "))
if play_a == "y":
    print("temp")

#print resualt 
if play_a == "n":
    print()
    print("-------------------------")
    print()
    print("A record of your results: ")
    print(results)

#INVAILD NUNBER

print("Thank you for using the Mathenator2000")