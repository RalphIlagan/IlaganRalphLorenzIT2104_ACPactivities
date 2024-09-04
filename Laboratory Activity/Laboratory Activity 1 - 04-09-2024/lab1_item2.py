characters= input("Enter two space - seperate characters: ")
ch1, ch2 = characters.split()
max_char = max(ch1,ch2)

print("---------------------------------------")
print(f"The caracter with greater value is: {max_char}")
print("---------------------------------------")
print("This part is optional to include.\n Showing ASCII Values: ")

print(f"{ch1} : {ord(ch1)}")
print(f"{ch2} : {ord(ch2)}")
