#Math triva game 
#Austin White 10/26/26
#ask the user there name and print a welcome message 

def welcome():
    name = input("What is your name? ")
    print(f"Greetings {name} welcome to the math triva game")
    return name
#question lists
def question():
    qs = ["Whats 1 + 1", ]
    a_s = ["1", ]

#Score
score = 0 
a = 0 
for q in qs:
