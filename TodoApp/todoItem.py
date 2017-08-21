
class TodoItem:


    def __init__(self, task_name, is_done = False):
        self.task_name = task_name
        self.is_done = is_done


    def do_task(self):
        self.is_done = True


    def __str__(self):
        if self.is_done:
            return "[x] " + self.task_name

        else:
            return "[ ] " + self.task_name



# task1 = TodoItem("Wyjdz z psem")
# #task1.do_task();
#
# print(task1)
