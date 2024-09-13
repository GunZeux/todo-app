import time
from modules.functions import get_todo, write_todo, complete_todos

while True:
    user_input = input("[+] Enter add, edit, show and complete: ").strip()

    todos = get_todo()

    if user_input.startswith("add"):
        todo = user_input[4:] + '\n'
        todos.append(todo)

    elif user_input.startswith("show"):
        for i, j in enumerate(todos):
            print(f"{i + 1} - {j}", end="")

    elif user_input.startswith("edit"):
        try:
            index = int(user_input[5:])
            todos[index - 1] = input("  [+] Enter new ToDO: ")+'\n'
        except ValueError:
            print("Enter a number followed by edit command eg Edit 3")
            continue
        except IndexError:
            print("Invalid index number")
            continue

    elif user_input.startswith("complete"):
        try:
            index = int(user_input[9:])
            removed_item = todos.pop(index - 1)

            time_local = time.asctime(time.localtime())
            removed_local = removed_item[:-1] + " - " + time_local+"\n"
            complete_todos(removed_local)

            print(f"  [+] ToDo {removed_item.strip()} was Completed Successfully")
        except ValueError:
            print("Enter a number followed by edit command eg complete 3")
            continue
        except IndexError:
            print("Invalid index number")
            continue

    elif user_input.startswith("exit"):
        print("Closing....")
        break

    else:
        print("[-] Unknown Command")

    write_todo(todos)
