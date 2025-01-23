new_students= input("enter a new name")

with open ("students.txt", "a") as file:
    file.write(new_students + "\n")
    