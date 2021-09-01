filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

new_file = " "
for line in lines:
    # Get rid of newline, then replace Python with C.
    print(line.rstrip().replace('Python',
                                'C'))  # Use rstrip() and replace() on the same line (chaining methods).
