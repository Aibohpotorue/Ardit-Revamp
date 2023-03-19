# from functions import get_todos(), write_todos # CLI stands for command-line interface.
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip() #strip is a method.
    user_action = user_action.lower()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos() #"files/todos.txt" removed as it has been changed to a default arguement at the top. Why declare it everytime if you only need to once?

        todos.append(todo.title() + '\n')

        functions.write_todos(todos_arg=todos) # Arguement, Arguement Values respectively. The variable declaration is optional. filepath has been ousted from arguements as it's declaration was set in the parameter section.

    elif user_action.startswith('show') or user_action.startswith('display'): #"Bitwise or opperator"
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}: {item}" # f    -string/formatting-string
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number -1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command isn't valid. Try something else.")
            continue
            
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            forthwith_ousted_todo = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Your {forthwith_ousted_todo} task has been completed and ousted from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue


    elif user_action.startswith('exit'):
        break

    else:
        print("Your command is not valid.")

#from functions import get_todos, write_todos

        # case _:
        #     print("Your response is not one of the listed commands.")

        
            # truncated_todos = [item.strip('\n') for item in todos] #List Comprehension

        # case 'add':
            #         file = open("files/todos.txt",'r')
            # todos = file.readlines()
            # file.close()

            #             file = open("files/todos.txt", 'w')
            # file.writelines(todos)
            # file.close()


# case 'show' | 'display':
            #             file = open("files/todos.txt", 'r')
            # todos = file.readlines()
            # file.close()

    # match user_action:
        # case 'add':
        # ...