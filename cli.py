import functions
import time

now = time.strftime("%b-%d-%Y, %H:%M:%S %p ")
print(f'It is: {now}')

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        # new_todos = [item.strip('\n') for item in todos] -> List Slicing

        for index, item in enumerate(todos, 1):
            no_space_item = item.replace('\n', '')
            print(f'{index}-{no_space_item}')

    elif user_action.startswith('edit'):

        try:
            todo_number = int(user_action[5:])
            todo_number -= 1
            todos = functions.get_todos()

            new_todo = input('Enter a new todo: ')
            todos[todo_number] = new_todo + '\n'
            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()

            todo_number = int(user_action[9:])
            todo_to_be_removed = todos[todo_number - 1].strip('\n')
            message = f"Todo: '{todo_to_be_removed}' was removed from the list."

            todos.pop(todo_number - 1)
            functions.write_todos(todos)

            print(message)

        except ValueError:
            print('Your command is not valid.')
            continue
        except IndexError:
            print(f"Todo #{user_action[9:]} does not exist.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("Bye!")
