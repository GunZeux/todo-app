import FreeSimpleGUI as fsg
import Zip_creator as archive

label_1 = fsg.Text("Source File")
label_2 = fsg.Text("Destination Dir")

input_box1 = fsg.InputText(tooltip="Enter Directory")
add_button1 = fsg.FilesBrowse("Choose", key="File")

input_box2 = fsg.InputText(tooltip="Enter Directory")
add_button2 = fsg.FolderBrowse("Choose", key="Folder")

compress_button = fsg.Button("Compress")
exit_button = fsg.Button("Exit")
output_label = fsg.Text(key="output", text_color="green")
windows = fsg.Window("Convert Files",
                     layout=[[label_1, input_box1, add_button1],
                             [label_2, input_box2, add_button2],
                             [compress_button, exit_button, output_label]])
while True:
    event, values = windows.read()
    if event == "Compress":
        filepaths = values["File"].split(";")
        destination = values["Folder"]
        archive.create_archive(filepaths, destination)
        windows["output"].update("FIle(s) Compressed Successfully")

    if event == fsg.WIN_CLOSED or event == "Exit":
        exit()


windows.close()