todos = []
while True:
    print("Add task - 1")
    print("Show tasks - 2")
    option = int(input())

    if option == 1:
        task = input()
        date = input()
        deadline = input()
        todo = [task, date, deadline]
        todos.append(todo)
        print("Task added!")

    elif option == 2:
        for i in todo:
            print(i)