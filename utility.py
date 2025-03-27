import csv

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Student(User):
    def __init__(self, username, password, first_name, last_name):
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Username: {self.username}"

class Instructor(User):
    def __init__(self, username, password, first_name, last_name, title):
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name
        self.title = title

    def __str__(self):
        return f"Instructor: {self.first_name} {self.last_name}, Title: {self.title}, Username: {self.username}"

class Course:
    def __init__(self, course_number, course_title, instructor):
        self.course_number = course_number
        self.course_title = course_title
        self.instructor = instructor

    def __str__(self):
        return f"Course: {self.course_number} - {self.course_title}, Instructor: {self.instructor.username}"

class AdminUtility:
    def __init__(self):
        self.admin_username = "admin"
        self.admin_password = "password"
        self.login_attempts = 5

    def login(self):
        while self.login_attempts > 0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == self.admin_username and password == self.admin_password:
                return True
            else:
                self.login_attempts -= 1
                print("Incorrect username or password. Please try again.")
                if self.login_attempts == 0:
                    print("You have exceeded the maximum number of login attempts. Exiting.")
                    exit()

    def run(self):
        if self.login():
            print("Login successful. Welcome, Admin!")
            # Proceed with admin functionalities
            pass

class StudentUtility:
    def __init__(self):
        pass

    def login(self):
        pass

    def run(self):
        pass

class InstructorUtility:
    def __init__(self):
        pass

    def login(self):
        pass

    def run(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()
