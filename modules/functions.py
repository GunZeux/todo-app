FILEPATH = "modules/todos.txt"
COM_FILEPATH = "modules/Completed.txt"


def get_todo(filepath=FILEPATH):
    """
    Read the text file and return
    the To Do list
    """
    with open(filepath, "r") as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todo(todos_arg, filepath=FILEPATH):
    """
    Write the given To Dos on the
    Text file present
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


def complete_todos(todos_arg, filepath=COM_FILEPATH):
    """
    Append the completed todos on the
    completed file
    """
    with open(filepath, "a") as file:
        file.write(todos_arg)
        file.close()


if __name__ == "__main__":
    print("From FUnction Module")

    print(get_todo("todos.txt"))
