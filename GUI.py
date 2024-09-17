import modules.functions as func
import FreeSimpleGUI as fsg
import time


fsg.theme("black")
clock = fsg.Text("", key='clock')
label = fsg.Text("type in a to do".title())
input_box = fsg.InputText(tooltip="Enter a todo".title(),
                          key="todo")

add_button = fsg.Button("Add")
listbox = fsg.Listbox(values=func.get_todo(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exi_button = fsg.Button("Exit")

window = fsg.Window("To Do App",
                    layout=[[clock], [label],
                            [input_box, add_button],
                            [listbox, edit_button, complete_button],
                            [exi_button]],
                    font=("Helvetica", 14))

while True:
    event, values = window.read(timeout=500)
    print(event)
    print(values)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = func.get_todo()
            new_todo = values["todo"] + "\n"

            if new_todo == "\n":
                fsg.popup("Enter a to do first", font=("Helvetica", 14))
                continue
            elif new_todo[:-1] in todos:
                fsg.popup("Todo already present in list")
                continue

            todos.append(new_todo)
            func.write_todo(todos)

            window["todos"].update(todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = func.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                func.write_todo(todos)

                window["todos"].update(todos)

            except IndexError:
                fsg.popup("Please Select An Item First", font=("Helvetica", 14))
            except ValueError:
                fsg.popup("Item Not Found in Data", font=("Helvetica", 14))

        case "todos":
            window["todo"].update(values["todos"][0])

        case "Complete":
            try:
                todo_complete = values['todos'][0]
                todos = func.get_todo()
                todos.remove(todo_complete)
                func.write_todo(todos)

                time_local = time.asctime(time.localtime())
                removed_local = todo_complete[:-1] + " - " + time_local + "\n"
                func.complete_todos(removed_local)

                window["todos"].update(todos)
                window['todo'].update(value='')

            except IndexError:
                fsg.popup("Please Select An Item First", font=("Helvetica", 14))
            except ValueError:
                fsg.popup("Item Not Found in Data", font=("Helvetica", 14))

        case "Exit":
            break

        case fsg.WIN_CLOSED:
            break


window.close()
