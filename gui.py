import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkBlack")   
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
label2 = sg.Text("Type in new edited to-do")
edit_input = sg.InputText(tooltip="New edited todo", key="todo_to_edit")
add_button = sg.Button("  Add  ", key="add_button", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("  Edit  ",key="edit_button", size=10)
complete_button = sg.Button("Complete", key="complete_button", size=10)
exit_button = sg.Button("Exit", key="exit_button", size=10)

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [label2],
                           [edit_input],
                           [list_box, [edit_button, complete_button]],
                           [exit_button]],
                   font=('Helvetica', 10)
                   )

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y Time: %H : %M : %S"))
   
    match event:
        case 'todos':
            try:
                window['todo_to_edit'].update(value=values['todos'][0])
            except IndexError:
                print("No items!")
            
        case "add_button":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            print(f"Todo: {new_todo}Status: Added succesfully!")
            
            window['todos'].update(values=todos)
            window['todo'].update(value="")
            
        case "edit_button": 
            try: 
                todo_to_edit = values['todos'][0]
                new_todo_to_edit = values['todo_to_edit']
                todos = functions.get_todos()       
                todo_index = todos.index(todo_to_edit)     
                todos[todo_index] = new_todo_to_edit + "\n"
                
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo_to_edit'].update(value="")
            except IndexError:
                sg.popup("Please select an item first to edit.")
                window['todo_to_edit'].update(value="")

        case "complete_button":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                
                window['todos'].update(values=todos)
                window['todo'].update(value="")
                window['todo_to_edit'].update(value="")

            except IndexError:
                sg.popup("Please select an item first to complete.")
                window['todo_to_edit'].update(value="")


        case "exit_button":
            break

        case sg.WIN_CLOSED:
            break

window.close()
