from functools import partial
from termcolor import colored, cprint

MENU_OPTIONS = ('View Tasks', 'Add a Task',
                'Remove a Task', 'Complete a Task', 'Exit')


def get_tasks():
    with open('./todo-list/tasks.txt', 'r') as file:
        content = file.read()
        tasks = content.split(',') if content.strip() else []

    with open('./todo-list/completed_tasks.txt', 'r') as file:
        content = file.read()
        completed_tasks = content.split(',') if content.strip() else []

    return (tasks, completed_tasks)


tasks, completed_tasks = get_tasks()


def get_choice(max_choice_value):
    while True:
        try:
            text = colored("Enter your choice: ", attrs=["bold", "blink"])
            choice = int(input(text).strip())

            if choice > max_choice_value or choice < 1:
                raise ValueError

            print()

            return choice
        except ValueError:
            print("Invalid choice")


def display_tasks():
    tasks_types = ('all', 'completed')

    while True:
        for number, tasks_type in enumerate(tasks_types, start=1):
            print(f"{number}. View {tasks_type} tasks")

        choice = get_choice(len(tasks_types))

        tasks_to_show = tasks if choice == 1 else completed_tasks

        if tasks_to_show:
            for number, task in enumerate(tasks_to_show, start=1):
                print(f"{number}. {task}")
            break
        else:
            cprint("Task list is empty!", 'red')
            break


def add_task():
    while True:
        task_name = input("Enter a new task: ").strip()

        if task_name:
            tasks.append(task_name)

            return

        print("Invalid name")


def manage_task(operation='remove'):
    while True:
        try:
            task_number = int(input("Enter the task number: "))

            if task_number < 1 or task_number > len(tasks):
                raise ValueError

            if operation == 'remove':
                completed_tasks.remove(tasks[task_number - 1])
                tasks.pop(task_number - 1)
            else:
                completed_tasks.append(tasks[task_number - 1])

            return
        except ValueError:
            print("Invalid task number")


def save_tasks(tasks, completed_tasks):
    with open('./todo-list/tasks.txt', 'w') as file:
        file.write(','.join(tasks))

    with open('./todo-list/completed_tasks.txt', 'w') as file:
        file.write(','.join(completed_tasks))


def main():
    options_total = len(MENU_OPTIONS)
    actions = (display_tasks, add_task, manage_task,
               partial(manage_task, 'complete'))

    while True:
        cprint('\nTodo List Menu:', color="yellow")

        for number, option in enumerate(MENU_OPTIONS, start=1):
            cprint(f"{number}. {option}", "light_cyan")

        choice = get_choice(options_total)

        if choice == options_total:
            break

        actions[choice - 1]()

    save_tasks(tasks, completed_tasks)


main()
