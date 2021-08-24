def show_magicians(names):
    """print each name of all magicians"""
    for name in names:
        print(name)


def make_great(names):
    for index in range(len(names)):
        names[index] = "the Great " + names[index]
    return names


magicians = ['lily', 'anna', 'milk']
modified_list = make_great(magicians[:])
print("\nThe original list is: ")
show_magicians(magicians)

print("\nThe modified list is: ")
show_magicians(modified_list)
