todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if 'add' in user_action:
        todo = user_action[4:]
        with open('Todos.txt','r') as file:
            todos = file.readlines()                
        todos.append(todo)
        with open('Todos.txt','w') as file:
            todos = file.writelines(todos)
    if 'show' in user_action:
        with open('Todos.txt','r') as file:
            todos = file.readlines()  
        new_todos = [o.strip('\n') for o in todos]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
    if 'edit' in user_action:
        number = int(input("Number of todo to edit: "))
        number = number - 1
        with open('Todos.txt','r') as file:
            todos = file.readlines()
        new_todo = input("Enter new todo: ").title()
        todos[number] = new_todo
        with open('Todos.txt','w') as file:
            todos = file.writelines(todos)
    if 'complete' in user_action:
        num = int(input("Number of todo to complete: "))
        with open('Todos.txt','r') as file:
            todos = file.readlines()
            index = num - 1
            todo_to_remove = todos[index]
        todos.pop(num - 1)
        with open('Todos.txt','w') as file:
            todos = file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
    if 'exit' in user_action:
        break
print("Bye!")
    

