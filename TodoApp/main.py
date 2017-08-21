from todoItem import TodoItem
from todoList import TodoList
import os



def main():
    clear_screen()
    todoList = TodoList()

    app_on = True

    while app_on:
        print_main_menu()
        option = input("Chose option: ")
        clear_screen()

        if option == "1":
            print_task_list(todoList)

        elif option == "2":
            task_name = input("Enter task name: ")
            new_task = TodoItem(task_name)
            todoList.add_task(new_task)

        elif option == "3":
            print_task_list(todoList)
            task_name = input("\nEnter task name: ")
            todoList = mark_task(task_name, todoList)

        elif option == "4":
            todoList.archive_tasks()

        elif option == "0":
            app_on = app_off()

        else:
            print("Wrong input")

        continue_button()
        clear_screen()


def print_main_menu():
    menu = "1. List tasks\n2. Add new task\n3. Mark task\n4. Arichive done tasks\n0. Exit app"
    print(menu)

def print_task_list(todoList):
    print(todoList)

def app_off():
    print("Bye :)")
    return False

def clear_screen():
    os.system('clear')

def mark_task(task_name, todoList):
    for task in todoList.todoList:
        if task.task_name == task_name:
            task.do_task()

    return todoList

def continue_button():
    input("Press any key to continue ...")




if __name__ == '__main__':
    main()
