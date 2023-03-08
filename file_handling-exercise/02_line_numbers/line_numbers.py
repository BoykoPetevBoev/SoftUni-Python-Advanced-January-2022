import re

with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for lineNumber, lineText in enumerate(input_file):
        stripped_line = lineText.strip()
        letters_count = len(re.findall('[A-Za-z]', stripped_line))
        marks_count = len(re.findall('[.,!\-\'":?]', stripped_line))
        output_file.write(f'Line {lineNumber+1}: {stripped_line} ({letters_count})({marks_count})\n')


