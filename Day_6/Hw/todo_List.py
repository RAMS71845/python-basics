task=[]
while True:
    print("\n---MENU---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit")

    choice=input("Choose Task (1-4): ")

    if choice=="1":
        new_task=input("Write your new task: ")
        task.append(new_task)
        print(f"'{new_task}'")

    elif choice=="2":
        if len(task)==0:
            print("Task menu is empty,Nothing to remove")
        else:
            print("Your tasks: ")
            for index, tasks in enumerate(task,start=1):
                print("f{index}.{tasks} ")

            user_no=int (input("which task has been completed?:  "))
            computer_no=user_no-1
            if computer_no>=0 and computer_no<len(task):
                removed_task=task.pop(computer_no)
                print(f"Congrats!! '{removed_task}' task has been completed.")
            else:
                print("You put the wrong task number.")
    elif choice =="3":
        if len(task)==0:
            print("Nothing task are there in the list.")  
        else:
            print ("\nYour tasks are: ")
            for index,tasks in enumerate(task,start=1):
                print(f"{index}.{tasks}")
    elif choice=="4":
        print("Application is closed!!!BYE BYE")
        break
    else:
        print("Wrong choice!,Choose Between 1 to 4: ")
