class Student:
    #Student object with some attributes
    def __init__(self, student_id, name, age, major):
        self.id = student_id
        self.name = name
        self.age = age
        self.major = major


class StudentDatabase:
    #student database with a list of adding,removing,update and finding a student
    def __init__(self):
        self.students = []
#A function of adding a student
    def add_student(self, student):
        self.students.append(student)

#A function of removing a student
    def remove_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)

#A function of updating a student
    def update_student(self, student_id, name=None, age=None, major=None):
        student = self.find_student(student_id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major

#A function of finding a student when you want to delete
    def find_student(self, student_id):
        self.id = student_id
        for student in self.students:
            if student.id == student_id:
                return student
            return None
    
    def get_all_students(self):
        return self.students


class StudentManagementSystem:
  #Student management system for managing all the information collected from the database
    def __init__(self, database):
        self.database = database

    def add_new_student(self, id, name, age, major):
        student = Student(id, name, age, major)
        self.database.add_student(student)

#A function deleting a student
    def delete_student(self, id):
        self.database.remove_student(id)

    def update_student_info(self, student_id, name=None, age=None, major=None):
        self.database.update_student(student_id, name, age, major)

#A function of display all student
    def show_all_students(self):
            students = self.database.get_all_students()
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Major: {student.major}")
#main function
def main_func():
    db = StudentDatabase()
    system = StudentManagementSystem(db)
#student menu system which allows user to choose..
    while True:
        print("\n\n1. add student")
        print("2. delete student")
        print("3. update student")
        print("4. view students")
        print("5. exit")
        choice = int(input("Enter choice: "))

#checking the condition statement if true it execute 
        if choice == 1:
            id = int(input("Enter student id:"))
            name = input("Enter student name:")
            age = int(input("Enter student age:"))
            major = input("Enter student major:")
            system.add_new_student(id,name,age,major)
            print("student added successfully")

        elif choice == 2:
            id = int(input("Enter student id:"))
            system.delete_student(id)
            print("student deleted successfully")

        elif choice == 3:
            id = int(input("Enter student id:"))
            name = input("Enter student name (or press enter for none):")
            age = int(input("Enter student age (or press enter for none):"))
            major = input("Enter student major (or press enter for none):")
            system.update_student_info(id, name=name or None, age=age or None, major=major or None)
            print("updated successfully")

        elif choice == 4:
            system.show_all_students()

        elif choice == 5:
            break

        #if the condition is not true it will execute
        else:
            print("invalid choice")


if __name__ == '__main__':
    main_func()