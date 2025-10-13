# Create a class Student with attributes: name, roll_no, and grade.
# Create 2 students and print their details.

class student: #defining the student class
    def __init__(self, name, roll_no, grade) :
        self.name=name
        self.roll_no=roll_no
        self.grade=grade

    def print_detais(self):#method to print student detais
        print(f"name: {self.name}, roll_no: {self.roll_no}, grade: {self.grade}")

#creating to objects for students
student1=student("dipendra", 28, "B+")
student2=student("sagar", 24, "c+")

#printing the detais 
student1.print_detais()
student2.print_detais()


# # # Define the Student class
# class Student:
#     def __init__(self, name, roll_no, grade):
#         self.name = name
#         self.roll_no = roll_no
#         self.grade = grade

#     def __str__(self):
#         return f"Name: {self.name}, Roll No: {self.roll_no}, Grade: {self.grade}"

# # Ask user how many students they want to enter
# num_students = int(input("How many students do you want to enter? "))

# students = []

# # Take input for each student
# for i in range(num_students):
#     print(f"\nEnter details for student {i+1}:")
#     name = input("Name: ")
#     roll_no = input("Roll No: ")
#     grade = input("Grade: ")
    
#     student = Student(name, roll_no, grade)
#     students.append(student)

# # Print all student details
# print("\nStudent Details:")
# for s in students:
#     print(s)



