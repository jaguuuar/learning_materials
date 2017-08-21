from todoItem import TodoItem

class TodoList:

    def __init__(self):
        self.todoList = []


    def add_task(self, new_task):
        self.todoList.append(new_task)


    def archive_tasks(self):
        uncomplited_tasks = []
        for task in self.todoList:
            if not task.is_done:
                uncomplited_tasks.append(task)

        self.todoList = uncomplited_tasks



    def __str__(self):
        string = ""
        count = 1

        for task in self.todoList:
            string += str(count) + ". " + str(task) + "\n"
            count += 1

        return string.strip()



# todoList = TodoList()
#
# task1 = TodoItem("Wyjdz z psem")
# task2 = TodoItem("Kup mleko")
# task3 = TodoItem("Napraw rower")
#
# todoList.add_task(task1)
# todoList.add_task(task2)
# todoList.add_task(task3)
#
# task2.do_task()
#
# todoList.archive_tasks()
# print(todoList)
