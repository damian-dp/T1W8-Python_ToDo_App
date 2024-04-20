import csv

def add_todo(file_name):
    print("\n")
    print("Add todo")
    todo_name = input("Enter a todo item: ")

    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print(view_todo(file_name))
    print("Remove List Item")
    todo_name = input("Enter the todo item name that you want to delete: ")
    
    # Create a new python list
    todo_lists = []

    # Put all the previous items into the list except the one they want to delete
    with open(file_name, "r") as f:
        reader = csv.reader(f)

        is_exist = False

        for row in reader: # [do grocery,False]
            if (todo_name != row[0]): # do laundry != do grocery -> True
                todo_lists.append(row) # [ [do grocery,False], [complete assignment,False] ]
            else:
                is_exist = True

    if not is_exist:
        print("\n")
        print("No item with that name exists. Please try again.")

    # Write the enter list.csv file with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def mark_todo():
    print("\n")
    print("Mark todo")

def view_todo(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f) # returns a nested list with lists as items

            # [
            #   [title,completed],
            #   [do grocery,False],
            #   [do laundry,False],
            #   [complete assignment,False]
            # ]

            reader.__next__() # Skips the first heading row so it doesnt show to user
            
            print("\n")
            print("\n")
            print("–––––––– YOUR TODO LIST ––––––––")

            for row in reader:
                if (row[1] == "True"):
                    print(f"{row[0]} is completed.")
                else:
                    print(f"{row[0]} is not complete.")

            print("\n")
            # print("–––––––––––––––––––––––––––––––––")
            # print("What would you like to do next?")

        
    except FileNotFoundError:
        print("\n")
        print("The todo file does not exist.")
