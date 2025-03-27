from admin import admin_module
from student import student_module
from instructor import instructor_module

def main():
    print("Welcome to Mini Canvas!")

    while True:
        print("\nSelect a module to access:")
        print("1. Admin Module")
        print("2. Student Module")
        print("3. Instructor Module")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin_module()
        elif choice == '2':
            student_module()
        elif choice == '3':
            instructor_module()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
