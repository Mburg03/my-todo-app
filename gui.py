import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
label2 = sg.Text("Type in new edited to-do")
edit_input = sg.InputText(tooltip="New edited todo", key="todo_to_edit")
add_button = sg.Button("  Add  ", key="add_button")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("  Edit  ",key="edit_button")
complete_button = sg.Button("Complete", key="complete_button")
exit_button = sg.Button("Exit", key="exit_button")

window = sg.Window('My To-Do App',
                   layout=[
                           [label],
                           [input_box, add_button],
                           [label2],
                           [edit_input],
                           [list_box, edit_button, complete_button],
                           [exit_button]
                           ],
                   font=('Helvetica', 10)
                   )

while True:
    event, values = window.read()
    print(1,event)    
    print(2,values)
    
    match event:
        case 'todos':
            window['todo_to_edit'].update(value=values['todos'][0])
            
        case "add_button":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            print(f"Todo: {new_todo}Status: Added succesfully!")
            
            window['todos'].update(values=todos)
            window['todo'].update(value="")
            
        case "edit_button": 
            todo_to_edit = values['todos'][0]
            new_todo_to_edit = values['todo_to_edit']
            todos = functions.get_todos()       
            todo_index = todos.index(todo_to_edit)     
            todos[todo_index] = new_todo_to_edit + "\n"
            
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo_to_edit'].update(value="")
            
        case "complete_button":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            
            window['todos'].update(values=todos)
            window['todo'].update(value="")
            
        case "exit_button":
            break
                
        case sg.WIN_CLOSED:
            break

window.close()
