from os import listdir, path


def traverse_dir(current_path, file_by_ext):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element),files_extensions)

        else:
            extension = element.split('.')[-1]
            if extension not in file_by_ext:
                file_by_ext[extension] = []
            file_by_ext[extension].append(element)


files_extensions = {}
traverse_dir('.',files_extensions)

for key, value in files_extensions.items():
    print(f'.{key}')
    for file in value:
        print(f'- - - {file}')
