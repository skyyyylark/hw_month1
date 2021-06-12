todo = []
while True:
    a = input("Plans, Add, Done: ")
    if a == "Plans" or a == "plans":
        for i in todo:
            print(i)
    elif a == "Add" or a == "add":
        num = input("Num of tasks: ")
        for i in range(int(num)):
            task = input("Task: ")
            start = input("Starting date: ")
            deadline = input("Deadline: ")
            todo.append([task, "starting date: " + start, "deadline: " + deadline])
            for i in todo:
                print(i)
    elif a == "Done" or a == "done":
        break
    else:
        print("Enter given options!")