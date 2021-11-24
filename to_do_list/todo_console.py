import os
import csv
from to_do_api import Task, ToDoList

# todo_console
DEFAULT = "todo_data.csv"


def clear_screen():
    os.system("cls")


def load_data(filepath=DEFAULT):
    final_task_list = []

    with open(filepath, 'r') as in_data:

        for _, row in enumerate(in_data):
            if _ == 0:
                continue
            if row == "\n":
                continue
            key, val, stat = row.strip().split(",")
            # all strings
            # print(key, val, stat)
            stat = True if stat == 'True' else False
            new_task = Task(val, stat)
            final_task_list.append(new_task)

    return final_task_list


def save_data_csv(data, filepath=DEFAULT):
    """ data = ToDoList.taskmap has random \n """
    with open(filepath, 'w', newline='') as out_data:
        todo_writer = csv.writer(out_data)

        indices = [
            "key",
            "value",
            "status"
        ]

        todo_writer.writerow(indices)
        for key, task in data.items():
            task_val, task_status = task.data_tuple()
            new_row = [
                key,
                task_val,
                task_status
            ]

            todo_writer.writerow(new_row)


def adding_task_menu(current_list: ToDoList):
    while True:
        clear_screen()
        print(current_list)
        user_task = input("\nInput task: ")

        # validate input
        if user_task.lower() == 'q':
            break
        # match user_task:
        # 	case "q":
        # 		break

        if current_list.add_task(Task(user_task)):
            print("\n[ added successfully ]")
        else:
            print("\n[ error 404: adding_task_menu ]\n")
            input("Press Enter to continue...")


def removing_task_menu(current_list: ToDoList):
    # Remove item loop
    while current_list.length != 0:
        extra_text = ""

        # Get Input
        u_in = input("\nSelect one to remove: ")

        # Validate Input
        if u_in.lower() == 'q':
            break

        # Status of Removal
        is_removed = current_list.remove_task(u_in)

        # Display Result
        clear_screen()
        print(current_list)

        if not is_removed:
            extra_text = "| Invalid index: Nothing Removed!"

        print(f"Size: {current_list.length} {extra_text}")

    if current_list.length == 0:
        clear_screen()
        print("[ EMPTY LIST ]\n\n")
        input("Press Enter to continue...")


def editing_task_menu(current_list: ToDoList):
    while True:
        clear_screen()
        print(current_list)

        user_choice = input("\nSelect task index to flip: ")

        # validate input
        if user_choice.lower() == 'q':
            break

        # match user_task:
        # 	case "q":
        # 		break

        if current_list.flip_mark(user_choice):
            print("\n[ changed successfully ]")
        else:
            print("\n[ error 404: editing_task_menu ]\n")
            input("Press Enter to continue...")


def saving_task_menu(current_list: ToDoList):
    clear_screen()
    new_file_path = input("Leave blank for Default: todo_data.csv\nSelect new path to save:")

    if new_file_path == "":
        save_data_csv(current_list.task_map)
    else:
        save_data_csv(current_list.task_map, new_file_path)

    print(f"\n[ Saved Successfully ]: {new_file_path}\n")
    input("Press Enter to continue...")


def loading_task_menu() -> ToDoList:
    clear_screen()
    new_file_path = input("Leave blank for Default: todo_data.csv\nSelect new path: ")
    if new_file_path == "":
        new_data = load_data()
    else:
        new_data = load_data(new_file_path)

    return ToDoList(new_data)


if __name__ == "__main__":
    # Get Screen Size
    width, height = os.get_terminal_size()

    load_file = input("Leave blank for Default: todo_data.csv\nSelect a file: ")

    if load_file == "":
        main_data = load_data()
    else:
        main_data = load_data(load_file)

    main_list = ToDoList(main_data, "Main Todo List")

    options = f"""Options:

 [A]: Add Task{5 * " "}[R]: Remove Task 
 
 [E]: Edit Status

 [S]: Save Data{4 * " "}[L]: Load Data
 
 [Q]: Quit
"""

    while True:
        # Display
        clear_screen()
        print(main_list)
        print(options)

        choice = input(">>> ")

        match choice:
            case "A" | 'a':
                adding_task_menu(main_list)

            case "R" | 'r':
                clear_screen()
                print(main_list)
                removing_task_menu(main_list)

            case "E" | 'e':
                editing_task_menu(main_list)

            case "S" | 's':
                saving_task_menu(main_list)

            case "L" | 'l':
                main_list = loading_task_menu()

            case "Q" | 'q':
                save = input("Would you like to save before you quit?: ")
                if save in ["y", "ye", "yes"]:
                    saving_task_menu(main_list)
                break

    print("\n[ Quit Program ]\n")
