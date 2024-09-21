# Mini Project: To-Do List

def welcome_interface():
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def what_to_do():
    what = input("What would you like to do? ").lower()
    if what == "1" or what == "add" or what == "add a task":
        return 1
    elif what == "2" or what == "view" or what == "view tasks":
        return 2
    elif what == "3" or what == "mark" or what == "mark a task as complete":
        return 3
    elif what == "4" or what == "delete" or what == "delete a task":
        return 4
    elif what == "5" or what == "quit":
        return 5
    else:
        return 0
    
def add_task():
    new_task = []
    new_task_1 = input("What task would you like to add to your list? ")
    new_task_2 = input("When is the task due? ")
    new_task.append(new_task_1.lower())
    new_task.append(new_task_2)
    new_task.append("Incomplete")
    tasks.append(new_task)
    print("Added task.")
    print("What else would you like to do?")

def view_tasks():
    if tasks == []:
        print("You don't have any tasks at the moment.\n")
    else:
        print("Sure. Here are your tasks:")
        for task in tasks:
            print(task)
    print("What else would you like to do?")

def mark_task():
    completed_task = input("Which task would you like to mark complete? ")
    found_task = False
    for task in tasks:
        if completed_task.lower() in task:
            found_task = True
            task[2] = "Complete"
        else:
            continue
    if found_task == False:
        print("Couldn't find that task.")

    print("What else would you like to do?")

def delete_task():
    task_to_delete = input("Which task would you like to delete? ")
    task_found = False
    for task in tasks:
        if task_to_delete.lower() in task:
            tasks.remove(task)
            print("Task deleted.")
            task_found = True
        else:
            continue
# Try/except would work here too, but I figured I didn't need to
    if task_found == False:
        print("Couldn't find that task.\n")

    print("What else would you like to do?")

def main_program():
    global keep_going
    do_what = what_to_do()
    if do_what == 1:
        add_task()
    elif do_what == 2:
        view_tasks()
    elif do_what == 3:
        mark_task()
    elif do_what == 4:
        delete_task()
    elif do_what == 5:
        print("\nThanks for using my program. I hope your experience was satisfactory...that'd be nice")
        keep_going = False
    elif do_what == 0:
        print("Invalid entry. Try a number from 1 to 5?")
    else:
        print("Oh no! Something went wrong.")

tasks = []
keep_going = True

print("Welcome to my To-Do List program!")
print()
while keep_going:
    welcome_interface()
    main_program()