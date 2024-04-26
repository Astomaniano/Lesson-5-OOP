class Task():
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.status = False

    def change_status(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False

class TaskList():
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline):
        task = Task(name, deadline)
        self.tasks.append(task)
        print(f'задача {name} добавлена на {deadline}')
    def mark_as_done(self, name):
        for task in self.tasks:
            if task.name == name:
                task.change_status()
                print(f'Задача {name} выполнена')
                break

    def get_current_tasks(self):
        current_tasks = []
        print('\nТекущие задачи:')
        for task in self.tasks:
            if task.status == False:
                current_tasks.append(task)
        for i in current_tasks:
            print(i.name, i.deadline)

    def all_tasks(self):
        print('\nВсе задачи:')
        for task in self.tasks:
            if task.status == False:
                print(task.name, task.deadline, "не выполнена")
            else:
                print(task.name, task.deadline, "выполнена")


work = TaskList()
work.add_task("помыть посуду", '10:00')
work.add_task("позвонить другу", '12:00')
work.add_task('пройти урок', '14:00')
work.add_task('поиграть в баскетбол', '16:00')

work.get_current_tasks()

work.mark_as_done('помыть посуду')

work.get_current_tasks()

work.all_tasks()


