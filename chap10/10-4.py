filename = 'guest_book.txt'

prompt = "\nTell me your name: "
prompt += "\nEnter 'quit' to end the program."
active = True

while active:
    name = input(prompt)
    if name == 'quit':
        break
    else:
        with open(filename, 'w') as f:
            f.write(name)
        print("Hi " + name + ", you've been added to the guest book.")
