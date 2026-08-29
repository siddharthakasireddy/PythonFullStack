from abc import ABC, abstractmethod

# Abstract Base Class
class Person(ABC):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Abstract method
    @abstractmethod
    def get_role(self):
        pass

    # Abstract method for full details
    @abstractmethod
    def get_full_details(self):
        pass

    # Common method
    def get_basic_info(self):
        return f"Name: {self._name}, Age: {self._age}"

    # Common method
    def get_details(self):
        return f"{self.get_basic_info()}, Role: {self.get_role()}"


# Student Class
class Student(Person):

    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self._student_id = student_id
        self._course = course

    # Implement abstract method
    def get_role(self):
        return "Student"

    # Student full details
    def get_full_details(self):
        return (
            f"{self.get_details()}, "
            f"Student ID: {self._student_id}, "
            f"Course: {self._course}"
        )


# Professor Class
class Professor(Person):

    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)
        self._emp_id = emp_id
        self._department = department

    # Implement abstract method
    def get_role(self):
        return "Professor"

    # Professor full details
    def get_full_details(self):
        return (
            f"{self.get_details()}, "
            f"Employee ID: {self._emp_id}, "
            f"Department: {self._department}"
        )


# Admin Staff Class
class AdminStaff(Person):

    def __init__(self, name, age, staff_id, designation):
        super().__init__(name, age)
        self._staff_id = staff_id
        self._designation = designation

    # Implement abstract method
    def get_role(self):
        return "Admin Staff"

    # Admin Staff full details
    def get_full_details(self):
        return (
            f"{self.get_details()}, "
            f"Staff ID: {self._staff_id}, "
            f"Designation: {self._designation}"
        )


# University Class
class University:

    # Class variable
    university_name = "ABC University"

    def __init__(self):
        # Private list
        self.__people = []

    # Add person to university
    def add_person(self, person: Person):
        self.__people.append(person)

    # Display all registered people
    def display_all(self):

        if not self.__people:
            print("No people registered yet.")

        else:
            for person in self.__people:
                print(person.get_full_details())

    # Class method
    @classmethod
    def get_university_name(cls):
        return cls.university_name

    # Static method
    @staticmethod
    def welcome_message():
        return "Welcome to the University Management System"


# ---------------- MAIN PROGRAM ----------------

print(University.welcome_message())
print("University:", University.get_university_name())


# Create University object
u = University()


# Menu
while True:

    print("\n--- University Menu ---")
    print("1. Register Student")
    print("2. Register Professor")
    print("3. Register Admin Staff")
    print("4. Display All People")
    print("0. Exit")

    ch = input("Choose an option: ")

    # Exit
    if ch == "0":

        print("Thank you! Exiting the system.")
        break

    # Register Student
    elif ch == "1":

        print("\n--- Register Student ---")

        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        student_id = input("Enter Student ID: ")
        course = input("Enter Course Name: ")

        s = Student(name, age, student_id, course)

        u.add_person(s)

        print("Student Registered Successfully!")


    # Register Professor
    elif ch == "2":

        print("\n--- Register Professor ---")

        name = input("Enter Professor Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        department = input("Enter Department: ")

        p = Professor(name, age, emp_id, department)

        u.add_person(p)

        print("Professor Registered Successfully!")


    # Register Admin Staff
    elif ch == "3":

        print("\n--- Register Admin Staff ---")

        name = input("Enter Staff Name: ")
        age = int(input("Enter Age: "))
        staff_id = input("Enter Staff ID: ")
        designation = input("Enter Designation: ")

        a = AdminStaff(name, age, staff_id, designation)

        u.add_person(a)

        print("Admin Staff Registered Successfully!")


    # Display all people
    elif ch == "4":

        print("\n--- List of Registered People ---")

        u.display_all()


    # Invalid option
    else:

        print("Invalid option. Please choose again.")
    