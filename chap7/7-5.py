prompt = "\nTell me your age:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("free")
        elif 3 <= age <= 12:
            print("10 $")
        elif age > 12:
            print("15 $")
