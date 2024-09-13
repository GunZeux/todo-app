import modules.functions
import FreeSimpleGUI as fsg


label = fsg.Text("type in a to do".title())
input_box = fsg.InputText(tooltip="Enter a todo".title())
add_button = fsg.Button("Add")

window = fsg.Window("To Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
