#Austin White
#10/28/26
#Sorting values is various ways
ls_name = []
name = ""
while name != "_DONE_":
    name = input("Enter a name (enter '_DONE_' to end): ")
    ls_name.append(name)
    if name == "_DONE_":
        ls_name.pop
        break
print(f"ORIGINAL - {ls_name}")

sorted_name = name.sort()
print(f"SORTED - {sorted_name}")
reversed_name = name
print(f"REVERSED - {reversed_name}")