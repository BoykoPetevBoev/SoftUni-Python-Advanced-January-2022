import os

while True:
    command_input = input()
    if command_input == 'End':
        break
    command_args = command_input.split('-')
    command = command_args[0]
    file_name = command_args[1]

    if command == 'Create':
        with open(file_name, 'w') as file:
            pass
    elif command == 'Add':
        content = command_args[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    elif command == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    elif command == 'Replace':
        old_string = command_args[2]
        new_string = command_args[3]
        if not os.path.exists(file_name):
            print("An error occurred")
            continue
        with open(file_name, 'r+') as file:
            new_file = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(new_file)

