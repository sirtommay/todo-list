#Tommy Chen 
#4th Period
#1/12/2024
#To Do List

#Intialize

todo = []

#Functions

#Makes todolist based on the 8 options a person chooses
# Tommy Chen 
def prompt():
    print("\nSelect an option \n1. Add Task To List \n2. View List \n3. Mark as Complete \n4. Remove Task \n5. Remove all tasks\n6. Sort alphabetically\n7. View number of items in list\n8. Exit Program")
    y = int(input("Option: "))
    if y == 1:
        todo.append(input("What do you want to add? "))
        prompt()
    elif y == 2:
        print(todo)
        prompt()
    elif y == 3:
        x = input("What did you complete? ")
        todo.remove(x)
        todo.append("X " + x)
        prompt()
    elif y == 4:
        todo.remove(input("What do you want to remove? "))
        prompt()
    elif y == 5:
        todo.clear()
        prompt()
    elif y == 6:
        todo.sort()
        prompt()
    elif y == 7:
        print(len(todo))
        prompt()
    else:
        quit()

#Main
        
prompt()