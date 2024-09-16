import modules.functions as func
import FreeSimpleGUI as fsg


label = fsg.Text("type in a to do".title())
input_box = fsg.InputText(tooltip="Enter a todo".title(),
                          key="todo")

add_button = fsg.Button("Add")
listbox = fsg.Listbox(values=func.get_todo(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = fsg.Button("Edit")

window = fsg.Window("To Do App",
                    layout=[[label], [input_box, add_button],[listbox, edit_button]],
                    font=("Helvetica", 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = func.get_todo()
            new_todo = values["todo"] + "\n"

            todos.append(new_todo)
            func.write_todo(todos)

            window["todos"].update(todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = func.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            func.write_todo(todos)

            window["todos"].update(todos)

        case "todos":
            window["todo"].update(values["todos"][0])

        case fsg.WIN_CLOSED:
            break;


window.close()
