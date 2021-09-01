class User():
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + ' ' + self.last_name
        self.age = age
        self.job = job

    def describe_user(self):
        print("The information of the user is:")
        print("The full name is: " + self.full_name.title())
        print("The age is: " + str(self.age))
        print("The job is: " + self.job)

    def greet_user(self):
        print("Hello, " + self.full_name.title() + "!\n")


user1 = User('jimi', 'hendrix', 32, 'teacher')
user1.describe_user()
user1.greet_user()

user2 = User('jay', 'chou', 18, 'singer')
user2.describe_user()
user2.greet_user()

user3 = User('rain', 'zhang', 40, 'actor')
user3.describe_user()
user3.greet_user()
