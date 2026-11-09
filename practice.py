#10/28/26
#Review for midterm
#Austin White

print("You'll add names to a list until your are done(Type DONE when finished) ")

#create a var call name (String)
name = ""

#Create a empty list named ls_names
ls_names = []

#make a While loop, until the user types "DONE" \
while name != "DONE":
    name = input("Add a name to the list: ")
    ls_names.append(name)
ls_names.pop 
print(f"Here's your list: {ls_names}")
#in the loop prompt the user for a input asking for the name 
#add the user input to the ls_names
