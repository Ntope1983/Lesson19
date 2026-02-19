import os

cwd = os.getcwd()
file_name = input(f"Give the name of the file u want to open (Example test.txt)\n")
menu = {1: "YES",
        2: "NO"}

try:
    with open(file_name, "r") as f:
        print("----------------------------------")
        print(f"{file_name} Found in Folder {cwd}")
except FileNotFoundError:
    print(f"{file_name} Not Found in Folder {cwd}\nDo u want to Create a file?")
    for option in menu:
        print(f"{option}: {menu[option]}")
    while True:
        try:
            value = int(input(f"Enter a number (1 to 2): "))
            if value == 1:
                with open(f"{file_name}", "w") as f:
                    f.write(f"{file_name} was created in {cwd}")
                break
            elif value == 2:
                print("Exit")
                break
            else:
                print(f"Number must be between 1 and 2.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
