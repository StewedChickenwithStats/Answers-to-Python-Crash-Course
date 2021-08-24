def show_magicians(names):
    """print each name of all magicians"""
    for name in names:
        print(name)


def make_great(names):
    for index in range(len(names)):
        names[index] = "the Great " + names[index]


magicians = ['lily', 'anna', 'milk']
make_great(magicians)
show_magicians(magicians)
