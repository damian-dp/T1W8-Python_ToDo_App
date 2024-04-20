# SYSTEM PACKAGES
import os.path

# EXTERNAL PACKAGES
from colored import Fore, Back, Style


# IMPORTS LOCAL FUNCTIONS
from todo_functions import add_todo, remove_todo, mark_todo, view_todo

print("\n")
print(f"{Fore.white}{Back.green} Welcome to your TODO list application {Style.reset}")

def create_menu():
    print("\n")
    print("1. Enter 1 to add item to the list")
    print("2. Enter 2 to remove item from the list")
    print("3. Enter 3 to mark any item as completed")
    print("4. Enter 4 to view todo list item")
    print("5. Enter 5 to exit")
    print("\n")

    user_choice = input("Enter your selection: ")
    # print(user_choice)
    return user_choice

file_name = "list.csv"


# If the file doesnt exist
if (not os.path.isfile(file_name)):

    print("\n")
    print("Creating file as it does not exist...")

    # Create the file
    todo_file = open(file_name, "w")

    # Enter the headings into the file
    todo_file.write("title,completed\n")

    # Close the file
    todo_file.close()


choice = ""

while choice != "5":
    choice = create_menu()


    if (choice == "1"):
        add_todo(file_name)

    elif (choice == "2"):
        remove_todo(file_name)

    elif (choice == "3"):
        mark_todo(file_name)

    elif (choice == "4"):
        view_todo(file_name)

    elif (choice == "5"):
        print("\n")
        print("You entered 5.")

    else:
        print("\n")
        print("Please only enter a number corresponding to the options below.")

print("Thanks for using our app. App has now been terminated")
