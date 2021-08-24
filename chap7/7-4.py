prompt = "\nTell me one topping on the pizza:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print("We will add "+message+" into your pizza.")
