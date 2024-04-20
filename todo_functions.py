import csv

def add_todo(file_name):
    print("\n")
    print("Add todo")
    todo_name = input("Enter a todo item: ")

    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo():
    print("\n")
    print("Remove todo")

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
            print("\n")

            for row in reader:
                if (row[1] == "True"):
                    print(f"{row[0]} is completed.")
                else:
                    print(f"{row[0]} is not complete.")

            print("\n")
            print("–––––––––––––––––––––––––––––––––")
            print("What would you like to do next?")

        
    except FileNotFoundError:
        print("\n")
        print("The todo file does not exist.")
