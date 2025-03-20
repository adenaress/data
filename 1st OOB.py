class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print(f"Student: {self.name}, ID: {self.student_id}, Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s new grade is {self.grade}.")

# Creating a student object
student1 = Student("Alice", "S1234", "B")

# Displaying student info
student1.display_info()  # Output: Student: Alice, ID: S1234, Grade: B

# Updating grade
student1.update_grade("A")  # Output: Alice's new grade is A.