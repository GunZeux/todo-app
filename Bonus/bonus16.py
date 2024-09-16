import FreeSimpleGUI as fsg


label_1 = fsg.Text("Source File")
label_2 = fsg.Text("Destination Dir")

input_box1 = fsg.InputText(tooltip="Enter Directory")
add_button1 = fsg.FileBrowse("Choose")

input_box2 = fsg.InputText(tooltip="Enter Directory")
add_button2 = fsg.FolderBrowse("Choose")

windows = fsg.Window("Convert Files",
                     layout=[[label_1, input_box1, add_button1],
                             [label_2, input_box2, add_button2]])
windows.read()
windows.close()