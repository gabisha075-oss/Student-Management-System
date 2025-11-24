class Student:
    def __init__(self, student_id, name, age, gender, dept, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.dept = dept
        self.marks = marks

    def to_string(self):
        return f"{self.student_id},{self.name},{self.age},{self.gender},{self.dept},{self.marks}"


class StudentManagement:
    def __init__(self, filename):
        self.filename = filename

    # ADD STUDENT
    def add_student(self):
        try:
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            dept = input("Enter Department: ")

            marks = input("Enter 3 marks separated by space: ")
            marks_list = list(map(int, marks.split()))

            if len(marks_list) != 3:
                print("Enter exactly 3 marks only.")
                return

            student = Student(student_id, name, age, gender, dept, marks_list)

            with open(self.filename, "a") as file:
                file.write(student.to_string() + "\n")

            print("Student added successfully!")

        except ValueError:
            print("Marks must be numbers only.")

    # VIEW STUDENTS
    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                data = file.readlines()

            if not data:
                print("No students found.")
                return

            for line in data:
                print(line.strip())

        except FileNotFoundError:
            print("No student file found.")

    # SEARCH
    def search_student(self, student_id):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    if line.startswith(student_id):
                        print("Student found:", line.strip())
                        return
            print("Student not found.")
        except FileNotFoundError:
            print("File not found.")

    # UPDATE STUDENT (supports updating ANY ONE field)
    def update_student(self, student_id):
        try:
            found = False
            students = []

            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[0] == student_id:
                        found = True

                        print("\nLeave blank and press ENTER to keep OLD value\n")

                        old_name = data[1]
                        old_age = data[2]
                        old_gender = data[3]
                        old_dept = data[4]
                        old_marks = eval(data[5])

                        new_name = input(f"New Name ({old_name}): ")
                        new_age = input(f"New Age ({old_age}): ")
                        new_gender = input(f"New Gender ({old_gender}): ")
                        new_dept = input(f"New Dept ({old_dept}): ")
                        new_marks = input(f"New Marks 3 values {old_marks}: ")

                        name = new_name if new_name else old_name
                        age = new_age if new_age else old_age
                        gender = new_gender if new_gender else old_gender
                        dept = new_dept if new_dept else old_dept

                        if new_marks:
                            marks = list(map(int, new_marks.split()))
                        else:
                            marks = old_marks

                        updated_student = Student(student_id, name, age, gender, dept, marks)
                        students.append(updated_student.to_string())

                    else:
                        students.append(line.strip())

        except FileNotFoundError:
            print("File not found.")
            return
        except ValueError:
            print("Marks should be numbers.")
            return

        if not found:
            print("Student not found.")
            return

        with open(self.filename, "w") as file:
            for s in students:
                file.write(s + "\n")

        print("Student updated successfully.")

    # DELETE
    def delete_student(self, student_id):
        try:
            new_data = []
            found = False

            with open(self.filename, "r") as file:
                for line in file:
                    if not line.startswith(student_id):
                        new_data.append(line)
                    else:
                        found = True

            if not found:
                print("Student not found.")
                return

            with open(self.filename, "w") as file:
                for line in new_data:
                    file.write(line)

            print("Student deleted successfully.")

        except FileNotFoundError:
            print("File not found.")

    # TOPPER
    def find_topper(self):
        try:
            topper_name = None
            topper_total = -1

            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    marks = eval(data[5])
                    total = sum(marks)

                    if total > topper_total:
                        topper_total = total
                        topper_name = data[1]

            if topper_name:
                print("Topper:", topper_name, "| Total:", topper_total)
            else:
                print("No students found.")

        except FileNotFoundError:
            print("File not found.")

    # AVERAGE
    def calculate_average(self):
        try:
            total_marks = [0, 0, 0]
            count = 0

            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    marks = eval(data[5])

                    total_marks[0] += marks[0]
                    total_marks[1] += marks[1]
                    total_marks[2] += marks[2]
                    count += 1

            if count == 0:
                print("No students found.")
                return

            print("\nAverage Marks:")
            print("Subject 1:", total_marks[0] / count)
            print("Subject 2:", total_marks[1] / count)
            print("Subject 3:", total_marks[2] / count)

        except FileNotFoundError:
            print("File not found.")


# MENU
def main():
    sm = StudentManagement("students.txt")

    while True:
        print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Find Topper\n7. Average Marks\n8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            sm.add_student()
        elif choice == "2":
            sm.view_students()
        elif choice == "3":
            sm.search_student(input("Enter Student ID: "))
        elif choice == "4":
            sm.update_student(input("Enter Student ID: "))
        elif choice == "5":
            sm.delete_student(input("Enter Student ID: "))
        elif choice == "6":
            sm.find_topper()
        elif choice == "7":
            sm.calculate_average()
        elif choice == "8":
            break
        else:
            print("Invalid choice!")


main()
