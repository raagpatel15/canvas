import csv

class AdminModule:
    def __init__(self):
        self.admin_credentials_file = 'admin_credentials.csv'
        self.student_file = 'students.csv'
        self.instructor_file = 'instructors.csv'
        self.course_file = 'courses.csv'
        self.enrollment_file = 'enrollments.csv'
        self.login_attempts_limit = 5

    def run(self):
        print("Welcome to the Admin Module")
        if not self.load_admin_credentials():
            print("Admin credentials file not found or empty.")
            return

        login_successful = False
        for _ in range(self.login_attempts_limit):
            username = input("Enter username: ")
            password = input("Enter password: ")
            if self.authenticate(username, password):
                login_successful = True
                break
            else:
                print("Incorrect username or password. Please try again.")

        if not login_successful:
            print("Too many login attempts. Exiting...")
            return

        print("Login successful. Welcome, Admin!")
        self.main_menu()

    def load_admin_credentials(self):
        try:
            with open(self.admin_credentials_file, 'r') as file:
                reader = csv.reader(file)
                self.admin_credentials = {row[0]: row[1] for row in reader}
                return True
        except FileNotFoundError:
            return False

    def authenticate(self, username, password):
        return username in self.admin_credentials and self.admin_credentials[username] == password

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Add a new student")
            print("2. Add an instructor")
            print("3. Add a new course")
            print("4. Add a course enrollment")
            print("5. See all student information")
            print("6. See all instructor information")
            print("7. See all course information")
            print("8. See all enrollment information")
            print("9. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_new_student()
            elif choice == '2':
                self.add_new_instructor()
            elif choice == '3':
                self.add_new_course()
            elif choice == '4':
                self.add_course_enrollment()
            elif choice == '5':
                self.see_all_student_information()
            elif choice == '6':
                self.see_all_instructor_information()
            elif choice == '7':
                self.see_all_course_information()
            elif choice == '8':
                self.see_all_enrollment_information()
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_student(self):
        pass  # Implement adding new student functionality

    def add_new_instructor(self):
        pass  # Implement adding new instructor functionality

    def add_new_course(self):
        pass  # Implement adding new course functionality

    def add_course_enrollment(self):
        pass  # Implement adding course enrollment functionality

    def see_all_student_information(self):
        pass  # Implement viewing all student information functionality

    def see_all_instructor_information(self):
        pass  # Implement viewing all instructor information functionality

    def see_all_course_information(self):
        pass  # Implement viewing all course information functionality

    def see_all_enrollment_information(self):
        pass  # Implement viewing all enrollment information functionality

if __name__ == "__main__":
    admin_module = AdminModule()
    admin_module.run()
