from modules import functions # Module and library used interchangably.
import PySimpleGUI as sg
import time
import os

if not os.path.exists('files/todos.txt'):
    with open('files/todos.txt', 'w') as file:
        pass

sg.theme('Black')

clock = sg.Text('', key="clock")

label = sg.Text('Type in a to-do:')
input_box = sg.InputText(tooltip='Enter a todo', key="todo")
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')

exit_button =  sg.Button('Exit')

window = sg.Window('Ardit To-Do App', # Each list is a seperate row.
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))


def feedback():
    window["todos"].update(values=todos)

def refresh():
    window["todo"].update(value='')


while True:
    try:
        event, values = window.read(timeout=200)
        window["clock"].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
        # print(1, event)
        # print(2, values)
        # print(3, values['todos'])
        match event:
            case "Add":
                todos = functions.get_todos()
                new_todo = values["todo"].strip() + '\n'
                todos.append(new_todo)
                functions.write_todos(todos)
                feedback()
                refresh()
            case "Edit":
                try:
                    todo_to_edit = values["todos"][0]
                    new_todo = values["todo"]
                    todos = functions.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + '\n'
                    functions.write_todos(todos)
                    feedback()
                    refresh()
                except IndexError:
                    sg.popup('Please select an item first.', font=('Helvetica', 20))
            case "Complete":
                try:
                    todo_to_complete = values["todos"][0]
                    todos = functions.get_todos()
                    todos.remove(todo_to_complete)
                    functions.write_todos(todos)
                    feedback()
                    refresh()
                except IndexError:
                    sg.popup('Please select an item first.', font=('Helvetica', 20))
            case "Exit":
                break
            case "todos":
                window["todo"].update(value=values["todos"][0])
            case sg.WIN_CLOSED:
                break
    except TypeError:
        break


window.close()

# add button = sg.Button(size=2, image_souce='images/add.png', mousover_colors='LightBlue2',
#                        tooltip='Add Todo', key='Add') # How to add images and colors to button.