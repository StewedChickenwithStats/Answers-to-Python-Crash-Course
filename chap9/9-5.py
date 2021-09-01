class User():
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + ' ' + self.last_name
        self.age = age
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        print("The information of the user is:")
        print("The full name is: " + self.full_name.title())
        print("The age is: " + str(self.age))
        print("The job is: " + self.job)

    def greet_user(self):
        print("Hello, " + self.full_name.title() + "!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


my_user = User('jimi', 'hendrix', 32, 'teacher')

my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(my_user.login_attempts)

my_user.reset_login_attempts()
print(my_user.login_attempts)
